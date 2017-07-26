from django.dispatch import Signal

create_student = Signal(providing_args=["instance"])
create_company = Signal(providing_args=["instance"])