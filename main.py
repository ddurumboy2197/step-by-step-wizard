class OnboardingWizard:
    def __init__(self):
        self.steps = [
            {"title": "Step 1: Registration", "description": "Please register to continue"},
            {"title": "Step 2: Profile Setup", "description": "Please set up your profile"},
            {"title": "Step 3: Account Verification", "description": "Please verify your account"},
            {"title": "Step 4: Onboarding Complete", "description": "You have completed the onboarding process"}
        ]
        self.current_step = 0

    def display_step(self):
        current_step = self.steps[self.current_step]
        print(f"Step {self.current_step + 1}: {current_step['title']}")
        print(current_step['description'])

    def next_step(self):
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
        else:
            print("Onboarding complete")

    def previous_step(self):
        if self.current_step > 0:
            self.current_step -= 1

wizard = OnboardingWizard()
while True:
    wizard.display_step()
    print("1. Next")
    print("2. Previous")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        wizard.next_step()
    elif choice == "2":
        wizard.previous_step()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
```

Kodda biz onboarding wizardi yaratdik, unda quyidagi funksiyalar mavjud:

- `display_step`: Joriy qadamni ko'rsatadi.
- `next_step`: Keyingi qadamga o'tadi.
- `previous_step`: Oldingi qadamga o'tadi.

Wizardda quyidagi qadamlar mavjud:

- Step 1: Registration
- Step 2: Profile Setup
- Step 3: Account Verification
- Step 4: Onboarding Complete

Foydalanuvchi wizardni boshlash uchun `1` ni tanlashi kerak, keyingi qadamga o'tish uchun `2` ni tanlashi kerak, oldingi qadamga o'tish uchun `3` ni tanlashi kerak. Foydalanuvchi wizardni tugatish uchun `4` ni tanlashi kerak.
