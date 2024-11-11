from faker import Faker

# Initialising Faker
fake = Faker()


def get_registered_user() -> dict:
    """
    Creating fake user details
    :returns: dict
    """
    return {
        "name": fake.name(),
        "address": fake.address(),
        "created_at": fake.year()
    }


# Running the file
if __name__ == "__main__":
    print(get_registered_user())
