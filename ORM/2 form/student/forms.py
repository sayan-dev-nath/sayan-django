from django import forms
from django.core.validators import MinLengthValidator


class Registration(forms.Form):
    first_name = forms.CharField(help_text="Write your first name")
    last_name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()


class Login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()


class Address(forms.Form):
    name = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    pin_code = forms.IntegerField()


# class DemoForm(forms.Form):
#     name = forms.CharField(
#         label="Full Name",  # ফিল্ডের নাম
#         max_length=100,  # সর্বোচ্চ অক্ষরের সংখ্যা
#         label_suffix=":",  # লেবেলের পরে কোলন
#         initial="Enter your full name",  # ফিল্ডে ডিফল্ট ভ্যালু দেখাবে
#         help_text="Enter your legal name here",  # ইউজারকে সাহায্য করার জন্য টেক্সট
#         validators=[MinLengthValidator(3)],  # ন্যূনতম ৩ অক্ষরের নাম লাগবে
#     )

#     email = forms.EmailField(
#         label="Email Address",  # ইমেইল লেবেল
#         disabled=True,  # ইউজার এই ফিল্ড এডিট করতে পারবে না
#     )

#     pin_code = forms.IntegerField(
#         label="Pin Code",  # পিন কোড নাম
#         min_value=100000,  # সর্বনিম্ন ৬ ডিজিট
#         max_value=999999,  # সর্বোচ্চ ৬ ডিজিট
#         error_messages={  # কাস্টম এরর মেসেজ
#             "min_value": "Pin code must be at least 6 digits",
#             "max_value": "Pin code can be at most 6 digits",
#         },
#     )

#     age = forms.FloatField(  # দশমিক সংখ্যায় বয়স নেওয়া
#         label="Age",
#         min_value=0,
#     )

#     data_of_birth = forms.DateField(  # জন্মতারিখ
#         label="Date of Birth",
#         required=False,  # এই ফিল্ড পূরণ না করলেও চলবে
#         help_text="Enter your birth date in YYYY-MM-DD format",
#     )

#     appointment_time = forms.TimeField(  # সময় নেওয়ার জন্য ফিল্ড
#         label="Appointment Time",
#         required=False,
#     )

#     appointment_datetime = forms.DateTimeField(  # সময় ও তারিখ একসাথে
#         label="Appointment Date & Time",
#         required=False,
#     )

#     is_subscribed = forms.BooleanField(  # চেকবক্স টাইপ ফিল্ড (True/False)
#         label="Subscribe to Newsletter",
#         required=False,
#     )

#     agree_terms = forms.NullBooleanField(  # তিনটা অবস্থা: True, False, বা None
#         label="Do you agree with terms?",
#     )

#     gender = forms.ChoiceField(  # সিঙ্গেল চয়েস
#         choices=[("m", "male"), ("f", "female"), ("o", "other")],
#         label="Gender",
#     )

#     interests = forms.MultipleChoiceField(  # একাধিক চয়েস সিলেক্ট করা যাবে
#         choices=[("t", "technology"), ("a", "art"), ("s", "sports")],
#         label="Interests",
#         required=False,
#     )

#     profile_image = forms.ImageField(  # ইমেজ আপলোড ফিল্ড
#         label="Profile Image",
#         required=False,
#     )

#     resume = forms.FileField(  # ফাইল আপলোড ফিল্ড (PDF, DOC ইত্যাদি)
#         label="Upload Resume",
#         required=False,
#     )

#     website = forms.URLField(  # ওয়েবসাইট URL ইনপুট
#         label="Personal Website",
#         required=False,
#     )

#     phone_number = forms.RegexField(  # ফোন নাম্বার নির্দিষ্ট ফরম্যাটে
#         regex=r"^(\+8801|01)[0-9]{9}$",  # বাংলাদেশের ফোন নাম্বার ফরম্যাট
#         error_messages={"invalid": "Enter a valid phone number, e.g., +8801812345678"},
#     )

#     password = forms.CharField(  # পাসওয়ার্ড ইনপুট
#         widget=forms.PasswordInput(),  # ইনপুট হাইড করে
#         label="Password",
#         max_length=50,
#         validators=[MinLengthValidator(8)],  # মিনিমাম ৮ ক্যারেক্টার
#         error_messages={"min_length": "Password must be at least 8 characters long."},
#     )

#     slug = forms.SlugField(  # ইউআরএল ফ্রেন্ডলি নাম (slug)
#         label="Slug",
#         max_length=50,
#     )

#     ip_address = forms.GenericIPAddressField(  # IPv4 বা IPv6 ইনপুট
#         label="IP Address",
#         protocol="both",  # উভয় ধরনের IP সাপোর্ট করে
#         unpack_ipv4=False,
#         localize=True,
#     )

#     rating = forms.DecimalField(  # দশমিক রেটিং ইনপুট (0.0 - 10.0)
#         label="Rating",
#         max_digits=3,  # সর্বোচ্চ ৩ ডিজিট (যেমন 10.0)
#         decimal_places=1,  # দশমিকের পরে ১ ঘর
#         min_value=0,
#         max_value=10,
#         initial=5.0,  # ডিফল্ট ভ্যালু
#         help_text="Provide a rating between 0 and 10",
#         localize=True,
#     )


class DemoForm(forms.Form):
    name = forms.CharField(
        label="CharField With TextInput",
        widget=forms.TextInput(attrs={"placeholder": "Type here..."}),
    )
    password = forms.CharField(
        label="Password Field",
        widget=forms.PasswordInput(attrs={"placeholder": "Enter password"}),
    )
    hidden_field = forms.CharField(
        label="Hidden Field",
        widget=forms.HiddenInput(),
    )
    email_field = forms.EmailField(
        label="Email Field",
        widget=forms.EmailInput(
            attrs={"placeholder": "name@example.com"},
        ),
    )
    url = forms.URLField(
        label="URL Field",
        widget=forms.URLInput(attrs={"placeholder": "https://example.com"}),
    )
    number = forms.IntegerField(
        label="Number Field",
        widget=forms.NumberInput(attrs={"min": "0", "max": "100"}),
    )
    date_field = forms.DateField(
        label="Date Field",
        widget=forms.DateInput(attrs={"type": "date", "placeholder": "YYYY-MM-DD"}),
    )
    time_field = forms.TimeField(
        label="Time Field",
        widget=forms.TimeInput(attrs={"type": "time", "placeholder": "HH:MM:SS"}),
    )
    date_time_field = forms.DateTimeField(
        label="DateTime Field",
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local", "placeholder": "YYYY-MM-DD HH:MM:SS"}
        ),
    )
    text_area = forms.CharField(
        label="Text Field",
        widget=forms.Textarea(attrs={"placeholder": "Enter multiple lines of text..."}),
    )
    boolean_field = forms.BooleanField(
        label="Boolean Field",
        widget=forms.CheckboxInput(),
    )
    null_boolean_field = forms.NullBooleanField(
        label="Null Boolean Field",
        widget=forms.NullBooleanSelect(),
    )
    choice_field = forms.ChoiceField(
        label="Choice Field",
        choices=[("1", "option 1"), ("2", "option 2"), ("3", "option 3")],
        widget=forms.Select(),
    )
    multiple_choice_field = forms.MultipleChoiceField(
        label="Multiple Choice Field",
        choices=[("1", "option 1"), ("2", "option 2"), ("3", "option 3")],
        widget=forms.SelectMultiple(),
    )
    radio_choice_field = forms.ChoiceField(
        label="Radio Choice Field",
        choices=[("1", "option 1"), ("2", "option 2"), ("3", "option 3")],
        widget=forms.RadioSelect(),
    )
    file_field = forms.FileField(
        label="File Field",
        widget=forms.FileInput(),
    )
    image_field = forms.ImageField(
        label="Image Field",
        widget=forms.ClearableFileInput(),
    )
    slug_field = forms.SlugField(
        label="Slug Field",
        widget=forms.TextInput(attrs={"placeholder": "my-slug"}),
    )
    ip_address_field = forms.GenericIPAddressField(
        label="IP Address Field",
        widget=forms.TextInput(attrs={"placeholder": "127.0.0.1"}),
    )
    time_duration_field = forms.DurationField(
        label="Duration Field",
        widget=forms.TextInput(attrs={"placeholder": "hh:mm:ss"}),
    )
    decimal_field = forms.DecimalField(
        label="Decimal Field",
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(attrs={"step": "0.1"}),
    )
    split_date_time = forms.SplitDateTimeField(
        label="Split Date Time Field", widget=forms.SplitDateTimeWidget()
    )
