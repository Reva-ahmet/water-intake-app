import flet as ft

def main(page: ft.Page):
    # App Settings
    page.title = "Water Intake Tracker"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 500

    # State variables
    goal = 2000
    current_water = 0

    # GUI Components
    title = ft.Text("Daily Hydration", size=30, weight=ft.FontWeight.BOLD)
    water_display = ft.Text(f"{current_water} / {goal} ml", size=20)
    progress_bar = ft.ProgressBar(value=0, width=300, color="blue")
    
    def add_water(e):
        nonlocal current_water
        if current_water < goal:
            current_water += 250
            # Update visuals
            progress_bar.value = current_water / goal
            water_display.value = f"{current_water} / {goal} ml"
            
            if current_water >= goal:
                water_display.value = "Goal Reached! 💧"
                water_display.color = "green"
            
            page.update()

    def reset(e):
        nonlocal current_water
        current_water = 0
        progress_bar.value = 0
        water_display.value = f"{current_water} / {goal} ml"
        water_display.color = None
        page.update()

    # Layout
    page.add(
        title,
        ft.Divider(height=20, color="transparent"),
        water_display,
        progress_bar,
        ft.Divider(height=20, color="transparent"),
        ft.ElevatedButton("Add 250ml", icon=ft.icons.WATER_DROP, on_click=add_water),
        ft.TextButton("Reset", on_click=reset, color="grey"),
        ft.Divider(height=40, color="transparent"),
        ft.Text("Final project submission by Reva", size=10, italic=True)
    )

if __name__ == "__main__":
    ft.app(target=main)