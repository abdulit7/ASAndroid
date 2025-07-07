# import flet as ft
# from assetpage import AssetFormPage

# class MyApp(ft.Container):
#     def __init__(self, page, **kwargs):  # Accept page as a parameter
#         super().__init__(**kwargs)
        
#         self.page = page  # Store the page object
#         self.padding = 20
#         self.bgcolor = ft.Colors.CYAN_100
#         self.border_radius = 10

#         self.add_asset_dialog = AssetFormPage(self.page, self)  # Pass the page object

#         self.asset_button = ft.ElevatedButton(
#             text="Add Asset",
#             on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             bgcolor=ft.Colors.BLUE_500,
#             color=ft.Colors.WHITE,
#             width=320,
#             height=50
#         )

#         self.component_button = ft.ElevatedButton(
#             text="Add Component",
#             #on_click=self.on_button_click,
#             bgcolor=ft.Colors.GREEN_500,
#             color=ft.Colors.WHITE,
#             width=320,
#             height=50
#         )

#         self.device_button = ft.ElevatedButton(
#             text="Add Device",
#             #on_click=self.on_button_click,
#             bgcolor=ft.Colors.RED_500,
#             color=ft.Colors.WHITE,
#             width=320,
#             height=50
#         )
#         self.consumable_button = ft.ElevatedButton(
#             text="Add Consumable",
#             #on_click=self.on_button_click,
#             bgcolor=ft.Colors.ORANGE_500,
#             color=ft.Colors.WHITE,
#             width=320,
#             height=50
#         )

#         self.content = ft.Column(
#             controls=[
#                 ft.Text("IT ASSET MANAGER", size=18, weight="bold"),
#                 self.asset_button,
#                 self.component_button,
#                 self.device_button,
#                 self.consumable_button,
#             ],
#             alignment=ft.MainAxisAlignment.CENTER,
#             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#         )


# def main(page: ft.Page):
#     page.title = "My Flet App"
#     page.window.width = 350
#     page.window.height = 600
#     page.add(MyApp(page))  # Pass the page object to MyApp
#     page.update()

# if __name__ == "__main__":
#     ft.app(target=main)


# import flet as ft
# from assetpage import AssetFormPage
# import sqlite3

# class MyApp(ft.Container):
#     def __init__(self, page, **kwargs):
#         super().__init__(**kwargs)
#         self.page = page
#         self.padding = 10
#         self.bgcolor = ft.Colors.CYAN_100
#         self.border_radius = 10

#         # Initialize SQLite3 database
#         self.local_db = sqlite3.connect("assets.db", check_same_thread=False)
#         self.initialize_local_db()

#         # Initialize AssetFormPage with camera and database
#         self.add_asset_dialog = AssetFormPage(self.page, self, allow_camera=True, local_db=self.local_db)

#         self.asset_button = ft.ElevatedButton(
#             text="Add Asset",
#             icon=ft.Icons.ADD,
#             on_click=lambda e: self.add_asset_dialog.open_dialog("asset"),
#             bgcolor=ft.Colors.BLUE_500,
#             color=ft.Colors.WHITE,
#             width=300,
#             height=50
#         )

#         self.component_button = ft.ElevatedButton(
#             text="Add Component",
#             icon=ft.Icons.BUILD,
#             on_click=lambda e: self.add_asset_dialog.open_dialog("component"),
#             bgcolor=ft.Colors.GREEN_500,
#             color=ft.Colors.WHITE,
#             width=300,
#             height=50
#         )

#         self.device_button = ft.ElevatedButton(
#             text="Add Device",
#             icon=ft.Icons.DEVICE_HUB,
#             on_click=lambda e: self.add_asset_dialog.open_dialog("device"),
#             bgcolor=ft.Colors.RED_500,
#             color=ft.Colors.WHITE,
#             width=300,
#             height=50
#         )

#         self.consumable_button = ft.ElevatedButton(
#             text="Add Consumable",
#             icon=ft.Icons.SHOPPING_BAG,
#             on_click=lambda e: self.add_asset_dialog.open_dialog("consumable"),
#             bgcolor=ft.Colors.ORANGE_500,
#             color=ft.Colors.WHITE,
#             width=300,
#             height=50
#         )

#         self.sync_button = ft.ElevatedButton(
#             text="Sync with Server",
#             icon=ft.Icons.SYNC,
#             on_click=self.sync_with_server,
#             bgcolor=ft.Colors.PURPLE_500,
#             color=ft.Colors.WHITE,
#             width=300,
#             height=50
#         )

#         self.content = ft.Column(
#             controls=[
#                 ft.Text("IT ASSET MANAGER", size=18, weight="bold", text_align=ft.TextAlign.CENTER),
#                 self.asset_button,
#                 self.component_button,
#                 self.device_button,
#                 self.consumable_button,
#                 self.sync_button,
#             ],
#             alignment=ft.MainAxisAlignment.CENTER,
#             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#             spacing=10,
#         )

#     def initialize_local_db(self):
#         cursor = self.local_db.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS assets (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 model TEXT,
#                 serial_number TEXT UNIQUE,
#                 company TEXT,
#                 location TEXT,
#                 purchase_date TEXT,
#                 status TEXT,
#                 last_sync TEXT
#             )
#         """)
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS asset_images (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 asset_id INTEGER,
#                 image_name TEXT,
#                 image_data BLOB,
#                 last_sync TEXT,
#                 FOREIGN KEY (asset_id) REFERENCES assets (id)
#             )
#         """)
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS asset_bills (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 asset_id INTEGER,
#                 bill_name TEXT,
#                 bill_data BLOB,
#                 last_sync TEXT,
#                 FOREIGN KEY (asset_id) REFERENCES assets (id)
#             )
#         """)
#         self.local_db.commit()

#     def sync_with_server(self, e):
#         self.add_asset_dialog.sync_with_server()
#         self.page.update()

# def main(page: ft.Page):
#     page.title = "IT Asset Manager"
#     page.window.width = 320
#     page.window.height = 600
#     page.theme_mode = ft.ThemeMode.LIGHT

#     app = MyApp(page)
#     page.add(app)
#     page.update()

# if __name__ == "__main__":
#     ft.app(target=main)


# import flet as ft
# from assetpage import AssetFormPage
# import sqlite3

# class MyApp(ft.Container):
#     def __init__(self, page, **kwargs):
#         super().__init__(**kwargs)
#         self.page = page
#         self.padding = 10
#         self.bgcolor = ft.Colors.CYAN_100
#         self.border_radius = 10

#         # Initialize SQLite3 database
#         self.local_db = sqlite3.connect("assets.db", check_same_thread=False)
#         self.initialize_local_db()

#         # Initialize AssetFormPage with camera and database
#         self.add_asset_dialog = AssetFormPage(self.page, self, local_db=self.local_db)

#         self.asset_button = ft.ElevatedButton(
#             text="Add Asset",
#             icon=ft.Icons.ADD,
#             on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             bgcolor=ft.Colors.BLUE_500,
#             color=ft.Colors.WHITE,
#             width=300,
#             height=50
#         )

#         self.component_button = ft.ElevatedButton(
#             text="Add Component",
#             icon=ft.Icons.BUILD,
#             on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             bgcolor=ft.Colors.GREEN_500,
#             color=ft.Colors.WHITE,
#             width=300,
#             height=50
#         )

#         self.device_button = ft.ElevatedButton(
#             text="Add Device",
#             icon=ft.Icons.DEVICE_HUB,
#             on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             bgcolor=ft.Colors.RED_500,
#             color=ft.Colors.WHITE,
#             width=300,
#             height=50
#         )

#         self.consumable_button = ft.ElevatedButton(
#             text="Add Consumable",
#             icon=ft.Icons.SHOPPING_BAG,
#             on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             bgcolor=ft.Colors.ORANGE_500,
#             color=ft.Colors.WHITE,
#             width=300,
#             height=50
#         )

#         self.sync_button = ft.ElevatedButton(
#             text="Sync with Server",
#             icon=ft.Icons.SYNC,
#             on_click=self.sync_with_server,
#             bgcolor=ft.Colors.PURPLE_500,
#             color=ft.Colors.WHITE,
#             width=300,
#             height=50
#         )

#         self.content = ft.Column(
#             controls=[
#                 ft.Text("IT ASSET MANAGER", size=18, weight="bold", text_align=ft.TextAlign.CENTER),
#                 self.asset_button,
#                 self.component_button,
#                 self.device_button,
#                 self.consumable_button,
#                 self.sync_button,
#             ],
#             alignment=ft.MainAxisAlignment.CENTER,
#             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#             spacing=10,
#         )

#     def initialize_local_db(self):
#         cursor = self.local_db.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS assets (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 model TEXT,
#                 serial_number TEXT UNIQUE,
#                 company TEXT,
#                 location TEXT,
#                 purchase_date TEXT,
#                 status TEXT,
#                 last_sync TEXT
#             )
#         """)
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS asset_images (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 asset_id INTEGER,
#                 image_name TEXT,
#                 image_data BLOB,
#                 last_sync TEXT,
#                 FOREIGN KEY (asset_id) REFERENCES assets (id)
#             )
#         """)
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS asset_bills (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 asset_id INTEGER,
#                 bill_name TEXT,
#                 bill_data BLOB,
#                 last_sync TEXT,
#                 FOREIGN KEY (asset_id) REFERENCES assets (id)
#             )
#         """)
#         self.local_db.commit()

#     def sync_with_server(self, e):
#         try:
#             self.add_asset_dialog.sync_with_server()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text("Sync with server completed!"),
#                 bgcolor=ft.Colors.GREEN_600
#             )
#             self.page.snack_bar.open = True
#         except Exception as ex:
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Sync error: {ex}"),
#                 bgcolor=ft.Colors.RED_600
#             )
#             self.page.snack_bar.open = True
#         self.page.update()

# def main(page: ft.Page):
#     page.title = "IT Asset Manager"
#     page.window.width = 320
#     page.window.height = 600
#     page.theme_mode = ft.ThemeMode.LIGHT

#     app = MyApp(page)
#     page.add(app)
#     page.update()

# if __name__ == "__main__":
#     ft.app(target=main)



# 




# import flet as ft
# from assetpage import AssetFormPage
# import sqlite3
# from asset import AssetPage

# class MyApp(ft.Container):
#     def __init__(self, page, **kwargs):
#         super().__init__(**kwargs)
#         self.page = page
#         self.padding = 0  # Remove padding from container to control it within layout

#         # Initialize SQLite3 database
#         self.local_db = sqlite3.connect("assets.db", check_same_thread=False)
#         self.initialize_local_db()

#         # Initialize AssetFormPage with camera and database
#         self.add_asset_dialog = AssetFormPage(self.page, self, local_db=self.local_db)

#         # Buttons
#         self.asset_button = ft.ElevatedButton(
#             text="Asset",
#             icon=ft.Icons.ADD,
#             on_click=lambda e: self.page.go(AssetPage(self.page)),
#             bgcolor=ft.Colors.BLUE_500,
#             color=ft.Colors.WHITE,
#             width=350,
#             height=50
#         )

#         self.component_button = ft.ElevatedButton(
#             text="Add Component",
#             icon=ft.Icons.BUILD,
#             on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             bgcolor=ft.Colors.GREEN_500,
#             color=ft.Colors.WHITE,
#             width=350,
#             height=50
#         )

#         self.device_button = ft.ElevatedButton(
#             text="Add Device",
#             icon=ft.Icons.DEVICE_HUB,
#             on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             bgcolor=ft.Colors.RED_500,
#             color=ft.Colors.WHITE,
#             width=350,
#             height=50
#         )

#         self.consumable_button = ft.ElevatedButton(
#             text="Add Consumable",
#             icon=ft.Icons.SHOPPING_BAG,
#             on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             bgcolor=ft.Colors.ORANGE_500,
#             color=ft.Colors.WHITE,
#             width=350,
#             height=50
#         )

#         self.sync_button = ft.ElevatedButton(
#             text="Sync with Server",
#             icon=ft.Icons.SYNC,
#             on_click=self.sync_with_server,
#             bgcolor=ft.Colors.PURPLE_500,
#             color=ft.Colors.WHITE,
#             width=350,
#             height=50
#         )

#         # Content Area with Border
#         self.content_area = ft.Container(
#             content=ft.Column(
#                 controls=[
#                     self.asset_button,
#                     self.component_button,
#                     self.device_button,
#                     self.consumable_button,
#                     self.sync_button,
#                 ],
#                 alignment=ft.MainAxisAlignment.CENTER,
#                 horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#                 spacing=10,
#             ),
#             border=ft.border.all(1, ft.Colors.GREY_400),
#             border_radius=10,
#             padding=10,
#             bgcolor=ft.Colors.WHITE,
#             width=350,
#             height=450,  # Adjusted height to fit within 600px with AppBar (60px) and BottomAppBar (80px)
#         )

#         # Main Layout
#         self.content = ft.Column(
#             controls=[
#                 self.content_area,
#             ],
#             expand=True,
#             spacing=0,
#         )

#     def initialize_local_db(self):
#         cursor = self.local_db.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS assets (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 model TEXT,
#                 serial_number TEXT UNIQUE,
#                 company TEXT,
#                 location TEXT,
#                 purchase_date TEXT,
#                 status TEXT,
#                 last_sync TEXT
#             )
#         """)
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS asset_images (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 asset_id INTEGER,
#                 image_name TEXT,
#                 image_data BLOB,
#                 last_sync TEXT,
#                 FOREIGN KEY (asset_id) REFERENCES assets (id)
#             )
#         """)
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS asset_bills (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 asset_id INTEGER,
#                 bill_name TEXT,
#                 bill_data BLOB,
#                 last_sync TEXT,
#                 FOREIGN KEY (asset_id) REFERENCES assets (id)
#             )
#         """)
#         self.local_db.commit()

#     def sync_with_server(self, e):
#         try:
#             self.add_asset_dialog.sync_with_server()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text("Sync with server completed!"),
#                 bgcolor=ft.Colors.GREEN_600
#             )
#             self.page.snack_bar.open = True
#         except Exception as ex:
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Sync error: {ex}"),
#                 bgcolor=ft.Colors.RED_600
#             )
#             self.page.snack_bar.open = True
#         self.page.update()

# def main(page: ft.Page):
#     page.title = "IT Asset Manager"
#     page.window.width = 350
#     page.window.height = 600
#     page.theme_mode = ft.ThemeMode.LIGHT

#     # Top AppBar
#     page.appbar = ft.AppBar(
#         title=ft.Text("IT ASSET MANAGER", size=18, weight="bold"),
#         bgcolor=ft.Colors.GREEN_300,
#         color=ft.Colors.WHITE,
#         center_title=True,
#         automatically_imply_leading=False,
#     )

#     # Floating Action Button
#     page.floating_action_button = ft.FloatingActionButton(
#         content=ft.Icon(ft.Icons.ADD, color=ft.Colors.BLUE_500),
#         bgcolor=ft.Colors.WHITE,
#         shape=ft.CircleBorder(),
#         on_click=lambda e: page.add_asset_dialog.open_dialog() if hasattr(page, 'add_asset_dialog') else None,
#     )
#     page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

#     # BottomAppBar with Menu Options in Menu Button
#     page.bottom_appbar = ft.BottomAppBar(
#         bgcolor=ft.Colors.BLUE,
#         shape=ft.NotchShape.CIRCULAR,
#         content=ft.Row(
#             controls=[
#                 ft.PopupMenuButton(
#                     items=[
#                         ft.PopupMenuItem(text="Option 1"),
#                         ft.PopupMenuItem(text="Option 2"),
#                         ft.PopupMenuItem(text="Option 3"),
#                         ft.PopupMenuItem(text="Option 4"),
#                     ],
#                     icon=ft.Icon(ft.Icons.MENU_BOOK, color=ft.Colors.WHITE),
#                     tooltip="Menu Options",
#                 ),
#                 ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE, tooltip="Search"),
#                 ft.Container(expand=True),  # Spacer to push "More" menu to the right
#                 # ft.PopupMenuButton(
#                 #     items=[
#                 #         ft.PopupMenuItem(text="Option 1"),
#                 #         ft.PopupMenuItem(text="Option 2"),
#                 #         ft.PopupMenuItem(text="Option 3"),
#                 #         ft.PopupMenuItem(text="Option 4"),
#                 #     ],
#                 #     icon=ft.Icon(ft.Icons.MORE_VERT, color=ft.Colors.WHITE),
#                 #     tooltip="More Options",
#                 # ),
#                 ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE, tooltip="Favorites"),
#             ],
#         ),
#     )

#     app = MyApp(page)
#     page.add(app)
#     page.update()

# if __name__ == "__main__":
#     ft.app(target=main)



# import flet as ft
# from assetpage import AssetFormPage
# import sqlite3
# from asset import AssetPage


# class MyApp(ft.Container):
#     def __init__(self, page, **kwargs):
#         super().__init__(**kwargs)
#         self.page = page
#         self.padding = 0  # Remove padding from container to control it within layout

#         # Initialize SQLite3 database
#         self.local_db = sqlite3.connect("assets.db", check_same_thread=False)
#         self.initialize_local_db()

#         # Initialize AssetFormPage with camera and database
#         self.add_asset_dialog = AssetFormPage(self.page, self, local_db=self.local_db)

#         # Buttons
#         self.asset_button = ft.ElevatedButton(
#             text="Asset",
#             icon=ft.Icons.ADD,
#             on_click=lambda e: self.page.go("/asset"),
#             bgcolor=ft.Colors.BLUE_500,
#             color=ft.Colors.WHITE,
#             width=300,
#             height=50
#         )

#         self.component_button = ft.ElevatedButton(
#             text="Add Component",
#             icon=ft.Icons.BUILD,
#             # on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             bgcolor=ft.Colors.GREEN_500,
#             color=ft.Colors.WHITE,
#             width=300,
#             height=50
#         )

#         self.device_button = ft.ElevatedButton(
#             text="Add Device",
#             icon=ft.Icons.DEVICE_HUB,
#             # on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             bgcolor=ft.Colors.RED_500,
#             color=ft.Colors.WHITE,
#             width=300,
#             height=50
#         )

#         self.consumable_button = ft.ElevatedButton(
#             text="Add Consumable",
#             icon=ft.Icons.SHOPPING_BAG,
#             # on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             bgcolor=ft.Colors.ORANGE_500,
#             color=ft.Colors.WHITE,
#             width=300,
#             height=50
#         )

#         self.sync_button = ft.ElevatedButton(
#             text="Sync with Server",
#             icon=ft.Icons.SYNC,
#             on_click=self.sync_with_server,
#             bgcolor=ft.Colors.PURPLE_500,
#             color=ft.Colors.WHITE,
#             width=300,
#             height=50
#         )

#         # Content Area with Border
#         self.content_area = ft.Container(
#             content=ft.Column(
#                 controls=[
#                     self.asset_button,
#                     self.component_button,
#                     self.device_button,
#                     self.consumable_button,
#                     self.sync_button,
#                 ],
#                 alignment=ft.MainAxisAlignment.CENTER,
#                 horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#                 spacing=10,
#             ),
#             border=ft.border.all(1, ft.Colors.GREY_400),
#             border_radius=10,
#             padding=10,
#             bgcolor=ft.Colors.WHITE,
#             width=320,
#             height=450,  # Adjusted height to fit within 600px with AppBar and BottomAppBar
#         )

#         # Main Layout
#         self.content = ft.Column(
#             controls=[
#                 self.content_area,
#             ],
#             expand=True,
#             spacing=0,
#         )

#     def initialize_local_db(self):
#         cursor = self.local_db.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS assets (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 model TEXT,
#                 serial_number TEXT UNIQUE,
#                 company TEXT,
#                 location TEXT,
#                 purchase_date TEXT,
#                 status TEXT,
#                 last_sync TEXT
#             )
#         """)
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS asset_images (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 asset_id INTEGER,
#                 image_name TEXT,
#                 image_data BLOB,
#                 last_sync TEXT,
#                 FOREIGN KEY (asset_id) REFERENCES assets (id)
#             )
#         """)
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS asset_bills (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 asset_id INTEGER,
#                 bill_name TEXT,
#                 bill_data BLOB,
#                 last_sync TEXT,
#                 FOREIGN KEY (asset_id) REFERENCES assets (id)
#             )
#         """)
#         self.local_db.commit()

#     def sync_with_server(self, e):
#         try:
#             self.add_asset_dialog.sync_with_server()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text("Sync with server completed!"),
#                 bgcolor=ft.Colors.GREEN_600
#             )
#             self.page.snack_bar.open = True
#         except Exception as ex:
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Sync error: {ex}"),
#                 bgcolor=ft.Colors.RED_600
#             )
#             self.page.snack_bar.open = True
#         self.page.update()

# # View factories dictionary
# VIEW_FACTORIES = {
#     "/": lambda p: MyApp(p),
#     "/asset": lambda p: AssetPage(p),
# }

# def main(page: ft.Page):
#     page.title = "IT Asset Manager"
#     page.window.width = 350
#     page.window.height = 600
#     page.theme_mode = ft.ThemeMode.LIGHT

#     # Top AppBar
#     page.appbar = ft.AppBar(
#         title=ft.Text("IT ASSET MANAGER", size=18, weight="bold"),
#         bgcolor=ft.Colors.GREEN_300,
#         color=ft.Colors.WHITE,
#         center_title=True,
#         automatically_imply_leading=False,
#     )

#     # Floating Action Button
#     page.floating_action_button = ft.FloatingActionButton(
#         content=ft.Icon(ft.Icons.ADD, color=ft.Colors.BLUE_500),
#         bgcolor=ft.Colors.WHITE,
#         shape=ft.CircleBorder(),
#         on_click=lambda e: page.add_asset_dialog.open_dialog() if hasattr(page, 'add_asset_dialog') else None,
#     )
#     page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

#     # BottomAppBar with Menu Options in Menu Button
#     page.bottom_appbar = ft.BottomAppBar(
#         bgcolor=ft.Colors.BLUE,
#         shape=ft.NotchShape.CIRCULAR,
#         content=ft.Row(
#             controls=[
#                 ft.PopupMenuButton(
#                     items=[
#                         ft.PopupMenuItem(text="Option 1"),
#                         ft.PopupMenuItem(text="Option 2"),
#                         ft.PopupMenuItem(text="Option 3"),
#                         ft.PopupMenuItem(text="Option 4"),
#                     ],
#                     icon=ft.Icon(ft.Icons.MENU_BOOK, color=ft.Colors.WHITE),
#                     tooltip="Menu Options",
#                 ),
#                 ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE, tooltip="Search"),
#                 ft.Container(expand=True),  # Spacer to push "More" menu to the right
#                 ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE, tooltip="Favorites"),
#             ],
#         ),
#     )

#     def change_route(e: ft.RouteChangeEvent):
#         """Handle route changes efficiently."""
#         route = e.route
#         print(f"Changing route to: {route}")
#         if route not in VIEW_FACTORIES:
#             route = "/"  # Default to main view if route is invalid

#         # Update content
#         new_content = VIEW_FACTORIES[route](page)
#         if isinstance(new_content, ft.Control):
#             page.views.clear()
#             page.views.append(
#                 ft.View(
#                     route=route,
#                     controls=[new_content],
#                     appbar=page.appbar,
#                     bottom_appbar=page.bottom_appbar,
#                 )
#             )
#         page.update()

#     # Attach event handlers
#     page.on_route_change = change_route
#     page.on_view_pop = lambda e: page.go(page.views[-1].route) if len(page.views) > 1 else None

#     # Initial view
#     page.go("/")

# if __name__ == "__main__":
#     ft.app(target=main)




# import flet as ft
# from home import Home
# from assetpage import AssetFormPage
# import sqlite3
# from asset import AssetPage

# # View factories dictionary
# VIEW_FACTORIES = {
#     "/": lambda p: Home(p),
#     "/asset": lambda p: AssetPage(p),
# }

# def main(page: ft.Page):
#     page.title = "IT Asset Manager"
#     page.window.width = 350
#     page.window.height = 600
#     page.theme_mode = ft.ThemeMode.LIGHT

#     # Top AppBar
#     page.appbar = ft.AppBar(
#         title=ft.Text("IT ASSET MANAGER", size=18, weight="bold"),
#         bgcolor=ft.Colors.GREEN_300,
#         color=ft.Colors.WHITE,
#         center_title=True,
#         automatically_imply_leading=False,
#     )

#     # Floating Action Button
#     page.floating_action_button = ft.FloatingActionButton(
#         content=ft.Icon(ft.Icons.ADD, color=ft.Colors.BLUE_500),
#         bgcolor=ft.Colors.WHITE,
#         shape=ft.CircleBorder(),
#         on_click=lambda e: page.add_asset_dialog.open_dialog() if hasattr(page, 'add_asset_dialog') else None,
#     )
#     page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

#     # BottomAppBar with Menu Options in Menu Button
#     page.bottom_appbar = ft.BottomAppBar(
#         bgcolor=ft.Colors.BLUE,
#         shape=ft.NotchShape.CIRCULAR,
#         content=ft.Row(
#             controls=[
#                 ft.PopupMenuButton(
#                     items=[
#                         ft.PopupMenuItem(text="Option 1"),
#                         ft.PopupMenuItem(text="Option 2"),
#                         ft.PopupMenuItem(text="Option 3"),
#                         ft.PopupMenuItem(text="Option 4"),
#                     ],
#                     icon=ft.Icon(ft.Icons.MENU_BOOK, color=ft.Colors.WHITE),
#                     tooltip="Menu Options",
#                 ),
#                 ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE, tooltip="Search"),
#                 ft.Container(expand=True),  # Spacer to push "More" menu to the right
#                 ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE, tooltip="Favorites"),
#             ],
#         ),
#     )

#     def change_route(e: ft.RouteChangeEvent):
#         """Handle route changes efficiently."""
#         route = e.route
#         print(f"Changing route to: {route}")
#         if route not in VIEW_FACTORIES:
#             route = "/"  # Default to main view if route is invalid

#         # Update content
#         new_content = VIEW_FACTORIES[route](page)
#         if isinstance(new_content, ft.Control):
#             page.views.clear()
#             page.views.append(
#                 ft.View(
#                     route=route,
#                     controls=[new_content],
#                     appbar=page.appbar,
#                     bottom_appbar=page.bottom_appbar,
#                 )
#             )
#         page.update()

#     # Attach event handlers
#     page.on_route_change = change_route
#     page.on_view_pop = lambda e: page.go(page.views[-1].route) if len(page.views) > 1 else None

#     # Initial view
#     page.go("/")

# if __name__ == "__main__":
#     ft.app(target=main)



# import flet as ft
# from home import Home
# from assetpage import AssetFormPage
# import sqlite3
# from asset import AssetPage

# # View factories dictionary
# VIEW_FACTORIES = {
#     "/": lambda p: Home(p),
#     "/asset": lambda p: AssetPage(p),
# }

# def main(page: ft.Page):
#     page.title = "IT Asset Manager"
#     page.window.width = 365
#     page.window.height = 600
#     page.window.min_width = 360  # Enforce minimum width
#     page.window.min_height = 600  # Enforce minimum height
#     page.theme_mode = ft.ThemeMode.LIGHT

#     # Top AppBar
#     page.appbar = ft.AppBar(
#         title=ft.Text("IT ASSET MANAGER", size=18, weight="bold"),
#         bgcolor=ft.Colors.GREEN_300,
#         color=ft.Colors.WHITE,
#         center_title=True,
#         automatically_imply_leading=False,
#     )

#     # Floating Action Button
#     page.floating_action_button = ft.FloatingActionButton(
#         content=ft.Icon(ft.Icons.ADD, color=ft.Colors.BLUE_500),
#         bgcolor=ft.Colors.WHITE,
#         shape=ft.CircleBorder(),
#         on_click=lambda e: page.add_asset_dialog.open_dialog() if hasattr(page, 'add_asset_dialog') else None,
#     )
#     page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

#     # BottomAppBar with Menu Options in Menu Button
#     page.bottom_appbar = ft.BottomAppBar(
#         bgcolor=ft.Colors.BLUE,
#         shape=ft.NotchShape.CIRCULAR,
#         content=ft.Row(
#             controls=[
#                 ft.PopupMenuButton(
#                     items=[
#                         ft.PopupMenuItem(text="Option 1"),
#                         ft.PopupMenuItem(text="Option 2"),
#                         ft.PopupMenuItem(text="Option 3"),
#                         ft.PopupMenuItem(text="Option 4"),
#                     ],
#                     icon=ft.Icon(ft.Icons.MENU_BOOK, color=ft.Colors.WHITE),
#                     tooltip="Menu Options",
#                 ),
#                 ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE, tooltip="Search"),
#                 ft.Container(expand=True),  # Spacer to push "More" menu to the right
#                 ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE, tooltip="Favorites"),
#             ],
#         ),
#     )

#     def change_route(e: ft.RouteChangeEvent):
#         """Handle route changes efficiently."""
#         route = e.route
#         print(f"Changing route to: {route}")
#         if route not in VIEW_FACTORIES:
#             route = "/"  # Default to main view if route is invalid

#         # Update content
#         new_content = VIEW_FACTORIES[route](page)
#         if isinstance(new_content, ft.Control):
#             page.views.clear()
#             page.views.append(
#                 ft.View(
#                     route=route,
#                     controls=[new_content],
#                     appbar=page.appbar,
#                     bottom_appbar=page.bottom_appbar,
#                 )
#             )
#         page.update()

#     def on_resize(e):
#         """Adjust layout on window resize."""
#         print(f"Resized to: {page.window.width}x{page.window.height}")
#         # Optionally adjust content sizes here if needed
#         page.update()

#     # Attach event handlers
#     page.on_route_change = change_route
#     page.on_view_pop = lambda e: page.go(page.views[-1].route) if len(page.views) > 1 else None
#     page.on_resize = on_resize

#     # Initial view
#     page.go("/")

# if __name__ == "__main__":
#     ft.app(target=main)


# import flet as ft
# from home import Home
# from assetpage import AssetFormPage
# import sqlite3
# from asset import AssetPage

# # View factories dictionary
# VIEW_FACTORIES = {
#     "/": lambda p: Home(p),
#     "/asset": lambda p: AssetPage(p),
# }

# def main(page: ft.Page):
#     page.title = "IT Asset Manager"
#     page.window.width = 365
#     page.window.height = 600
#     page.window.min_width = 360
#     page.window.min_height = 600
#     page.theme_mode = ft.ThemeMode.LIGHT

#     # Top AppBar
#     page.appbar = ft.AppBar(
#         title=ft.Text("IT ASSET MANAGER", size=18, weight="bold"),
#         bgcolor=ft.Colors.GREEN_300,
#         color=ft.Colors.WHITE,
#         center_title=True,
#         automatically_imply_leading=False,
#     )

#     # Floating Action Button
#     page.floating_action_button = ft.FloatingActionButton(
#         content=ft.Icon(ft.Icons.ADD, color=ft.Colors.BLUE_500),
#         bgcolor=ft.Colors.WHITE,
#         shape=ft.CircleBorder(),
#         on_click=lambda e: page.go("/asset") if hasattr(page, 'views') else None,
#     )
#     page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

#     # BottomAppBar with Menu Options in Menu Button
#     page.bottom_appbar = ft.BottomAppBar(
#         bgcolor=ft.Colors.BLUE,
#         shape=ft.NotchShape.CIRCULAR,
#         content=ft.Row(
#             controls=[
#                 ft.PopupMenuButton(
#                     items=[
#                         ft.PopupMenuItem(text="Option 1"),
#                         ft.PopupMenuItem(text="Option 2"),
#                         ft.PopupMenuItem(text="Option 3"),
#                         ft.PopupMenuItem(text="Option 4"),
#                     ],
#                     icon=ft.Icon(ft.Icons.MENU_BOOK, color=ft.Colors.WHITE),
#                     tooltip="Menu Options",
#                 ),
#                 ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE, tooltip="Search"),
#                 ft.Container(expand=True),
#                 ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE, tooltip="Favorites"),
#             ],
#         ),
#     )

#     def change_route(e: ft.RouteChangeEvent):
#         route = e.route
#         print(f"Changing route to: {route}")
#         if route not in VIEW_FACTORIES:
#             route = "/"
#         new_content = VIEW_FACTORIES[route](page)
#         page.views.clear()
#         page.views.append(
#             ft.View(
#                 route=route,
#                 controls=[new_content],
#                 appbar=page.appbar,
#                 bottom_appbar=page.bottom_appbar,
#             )
#         )
#         page.update()

#     def on_resize(e):
#         print(f"Resized to: {page.window.width}x{page.window.height}")
#         page.update()

#     page.on_route_change = change_route
#     page.on_view_pop = lambda e: page.go(page.views[-1].route) if len(page.views) > 1 else None
#     page.on_resize = on_resize

#     page.go("/")

# if __name__ == "__main__":
#     ft.app(target=main)



import flet as ft
from home import Home
from assetpage import AssetFormPage
import sqlite3
from asset import AssetPage
from sync_server import initialize_local_db

# View factories dictionary
VIEW_FACTORIES = {
    "/": lambda p: Home(p),
    "/asset": lambda p: AssetPage(p),
}

def main(page: ft.Page):
    page.title = "IT Asset Manager"
    page.window.width = 365
    page.window.height = 600
    page.window.min_width = 360
    page.window.min_height = 600
    page.theme_mode = ft.ThemeMode.LIGHT

    # Top AppBar
    page.appbar = ft.AppBar(
        title=ft.Text("IT ASSET MANAGER", size=18, weight="bold"),
        bgcolor=ft.Colors.GREEN_300,
        color=ft.Colors.WHITE,
        center_title=True,
        automatically_imply_leading=False,
    )

    # Floating Action Button
    page.floating_action_button = ft.FloatingActionButton(
        content=ft.Icon(ft.Icons.ADD, color=ft.Colors.BLUE_500),
        bgcolor=ft.Colors.WHITE,
        shape=ft.CircleBorder(),
        on_click=lambda e: page.go("/asset") if hasattr(page, 'views') else None,
    )
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    # BottomAppBar with Menu Options in Menu Button
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.Colors.BLUE,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Option 1"),
                        ft.PopupMenuItem(text="Option 2"),
                        ft.PopupMenuItem(text="Option 3"),
                        ft.PopupMenuItem(text="Option 4"),
                    ],
                    icon=ft.Icon(ft.Icons.MENU_BOOK, color=ft.Colors.WHITE),
                    tooltip="Menu Options",
                ),
                ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE, tooltip="Search"),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE, tooltip="Favorites"),
            ],
        ),
    )

    def change_route(e: ft.RouteChangeEvent):
        route = e.route
        print(f"Changing route to: {route}")
        if route not in VIEW_FACTORIES:
            route = "/"
        new_content = VIEW_FACTORIES[route](page)
        page.views.clear()
        page.views.append(
            ft.View(
                route=route,
                controls=[new_content],
                appbar=page.appbar,
                bottom_appbar=page.bottom_appbar,
            )
        )
        page.update()

    def on_resize(e):
        print(f"Resized to: {page.window.width}x{page.window.height}")
        page.update()

    page.on_route_change = change_route
    page.on_view_pop = lambda e: page.go(page.views[-1].route) if len(page.views) > 1 else None
    page.on_resize = on_resize

    page.go("/")

if __name__ == "__main__":
    ft.app(target=main)