from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from .forms import CustomUserCreationForm
from .models import Item, ChangeLog, Tag, Comment
import os


# List all items
@login_required
def item_list(request):
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

    # Inicializamos la búsqueda con todos los ítems
    items = Item.objects.all().order_by("-created_at")

    # Búsqueda por texto en nombre o descripción
    search_query = request.GET.get("search", "")
    if search_query:
        items = items.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )

    # Filtro por usuario creador
    creator_filter = request.GET.get("creator", "")
    if creator_filter:
        items = items.filter(created_by__username=creator_filter)

    # Filtro por tipo de archivo
    file_filter = request.GET.get("file_type", "")
    if file_filter == "with_file":
        items = items.exclude(file="")
    elif file_filter == "with_image":
        # Esta es una aproximación, idealmente usaríamos un método más sofisticado
        items = items.exclude(file="").filter(
            Q(file__iendswith=".jpg")
            | Q(file__iendswith=".jpeg")
            | Q(file__iendswith=".png")
            | Q(file__iendswith=".gif")
        )
    elif file_filter == "without_file":
        items = items.filter(file="")

    # Filtro por etiqueta
    tag_filter = request.GET.get("tag", "")
    if tag_filter:
        items = items.filter(tags__name=tag_filter)

    # Paginación
    page = request.GET.get("page", 1)
    paginator = Paginator(items, 10)  # Mostrar 10 ítems por página

    try:
        items_page = paginator.page(page)
    except PageNotAnInteger:
        # Si page no es un entero, muestra la primera página
        items_page = paginator.page(1)
    except EmptyPage:
        # Si page está fuera de rango, muestra la última página de resultados
        items_page = paginator.page(paginator.num_pages)

    # Obtener lista de usuarios para el filtro
    creators = User.objects.filter(items__isnull=False).distinct()

    # Obtener todas las etiquetas para el filtro
    all_tags = Tag.objects.all()

    context = {
        "items": items_page,
        "search_query": search_query,
        "creator_filter": creator_filter,
        "file_filter": file_filter,
        "tag_filter": tag_filter,
        "creators": creators,
        "all_tags": all_tags,
    }

    return render(request, "item_list.html", context)


# Create a new item
@login_required
def item_create(request):
    # Obtener todas las etiquetas para mostrar en el formulario
    all_tags = Tag.objects.all().order_by("name")

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        item = Item.objects.create(
            name=name, description=description, created_by=request.user
        )

        # Manejar la subida de archivo si existe
        if "file" in request.FILES:
            item.file = request.FILES["file"]
            item.save()

        # Manejar etiquetas existentes seleccionadas
        if "tags" in request.POST:
            selected_tags = request.POST.getlist("tags")
            for tag_id in selected_tags:
                try:
                    tag = Tag.objects.get(id=tag_id)
                    item.tags.add(tag)
                except Tag.DoesNotExist:
                    pass

        # Manejar nuevas etiquetas
        new_tags = request.POST.get("new_tags", "")
        if new_tags:
            tag_names = [tag.strip() for tag in new_tags.split(",") if tag.strip()]
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                item.tags.add(tag)

        # Crear registro en el historial con datos adicionales
        ChangeLog.objects.create(
            item=item,
            item_name=item.name,
            original_item_id=item.id,
            user=request.user,
            action="create",
            additional_data={"description": item.description},
        )
        return redirect("item_list")

    context = {"all_tags": all_tags}
    return render(request, "item_form.html", context)


# Update an existing item
@login_required
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    # Obtener todas las etiquetas para mostrar en el formulario
    all_tags = Tag.objects.all().order_by("name")

    if request.method == "POST":
        old_name = item.name
        old_description = item.description

        item.name = request.POST.get("name")
        item.description = request.POST.get("description")

        # Manejar la subida de archivo si existe
        if "file" in request.FILES:
            if item.file:
                # Eliminar archivo antiguo si hay uno nuevo
                if os.path.isfile(item.file.path):
                    os.remove(item.file.path)
            item.file = request.FILES["file"]

        # Verificar si se debe eliminar el archivo
        if request.POST.get("remove_file") and item.file:
            file_path = item.file.path
            if os.path.isfile(file_path):
                os.remove(file_path)
            item.file = None

        # Guardar cambios básicos antes de manejar etiquetas
        item.save()

        # Manejar etiquetas - primero limpiar las existentes
        item.tags.clear()

        # Añadir etiquetas existentes seleccionadas
        if "tags" in request.POST:
            selected_tags = request.POST.getlist("tags")
            for tag_id in selected_tags:
                try:
                    tag = Tag.objects.get(id=tag_id)
                    item.tags.add(tag)
                except Tag.DoesNotExist:
                    pass

        # Manejar nuevas etiquetas
        new_tags = request.POST.get("new_tags", "")
        if new_tags:
            tag_names = [tag.strip() for tag in new_tags.split(",") if tag.strip()]
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                item.tags.add(tag)

        # Crear registro en el historial con datos adicionales
        ChangeLog.objects.create(
            item=item,
            item_name=item.name,
            original_item_id=item.id,
            user=request.user,
            action="update",
            additional_data={
                "old_name": old_name,
                "old_description": old_description,
                "new_name": item.name,
                "new_description": item.description,
            },
        )
        return redirect("item_list")

    context = {"item": item, "all_tags": all_tags}
    return render(request, "item_form.html", context)


# Delete an item
@login_required
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        # Guardar información del ítem antes de eliminarlo
        item_name = item.name
        item_id = item.id
        item_description = item.description

        # Crear registro en el historial con datos adicionales
        ChangeLog.objects.create(
            item=None,  # El ítem se eliminará, así que no habrá referencia
            item_name=item_name,
            original_item_id=item_id,
            user=request.user,
            action="delete",
            additional_data={
                "description": item_description,
                "created_by": request.user.username,
            },
        )

        # Ahora se puede eliminar el ítem
        item.delete()
        return redirect("item_list")
    return render(request, "item_confirm_delete.html", {"item": item})


# Edit user profile
@login_required
def edit_profile(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get("first_name", user.first_name)
        user.last_name = request.POST.get("last_name", user.last_name)
        user.email = request.POST.get("email", user.email)
        user.save()
        messages.success(request, "Profile updated successfully!")

        # Redirect to the item list page after saving changes
        return redirect("item_list")

    return render(request, "edit_profile.html", {"next": request.GET.get("next", "")})


# Register a new user
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


# Change log list (for administrators)
@staff_member_required
def change_log_list(request):
    change_logs = ChangeLog.objects.select_related("item", "user").order_by(
        "-timestamp"
    )
    return render(request, "change_log_list.html", {"change_logs": change_logs})


# Item detail view
@login_required
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    comments = item.comments.all()

    # Historial de cambios para este ítem
    changes = ChangeLog.objects.filter(
        Q(item=item) | Q(original_item_id=item.id, item__isnull=True)
    ).order_by("-timestamp")

    # Manejar la publicación de un nuevo comentario
    if request.method == "POST":
        comment_text = request.POST.get("comment_text", "").strip()
        if comment_text:
            Comment.objects.create(item=item, user=request.user, text=comment_text)
            messages.success(request, "Comment added successfully!")
            return redirect("item_detail", pk=pk)
        else:
            messages.error(request, "Comment cannot be empty.")

    context = {"item": item, "comments": comments, "changes": changes}

    return render(request, "item_detail.html", context)
