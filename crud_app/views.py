from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CustomUserCreationForm
from .models import Item, ChangeLog


# List all items
@login_required
def item_list(request):
    items = Item.objects.all()
    return render(request, "item_list.html", {"items": items})


# Create a new item
@login_required
def item_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        item = Item.objects.create(
            name=name, description=description, created_by=request.user
        )

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
    return render(request, "item_form.html")


# Update an existing item
@login_required
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        old_name = item.name
        old_description = item.description

        item.name = request.POST.get("name")
        item.description = request.POST.get("description")
        item.save()

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
    return render(request, "item_form.html", {"item": item})


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
