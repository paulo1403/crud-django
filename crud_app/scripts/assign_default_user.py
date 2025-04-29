from django.contrib.auth.models import User
from crud_app.models import Item

def assign_default_user():
    # Get the first user in the database as the default user
    default_user = User.objects.first()
    if not default_user:
        print("No users found in the database. Please create a user first.")
        return

    # Assign the default user to items with no created_by
    items_without_user = Item.objects.filter(created_by__isnull=True)
    for item in items_without_user:
        item.created_by = default_user
        item.save()

    print(f"Assigned default user '{default_user.username}' to {items_without_user.count()} items.")

if __name__ == "__main__":
    assign_default_user()
