# import os
# os.environ["FLET_SECRET_KEY"] = "mysecret123"
# import flet as ft
# import mysql.connector
# from mysql.connector import Error
# import base64
# # from components.assetformpage import AssetFormPage
# # from components.assetformmanage import AssetFormManage

# class AssetPage(ft.Container):
#     def __init__(self, page: ft.Page):
#         super().__init__()

#         self.page = page
#         self.page.title = "Asset Management"
#         self.page.window_title = "Asset Management"
#         self.page.window.width = 320
#         self.page.window.height = 600

#         self.expand = True
#         self.asset_add = []

#         # Initialize dialogs with self as parent
#         # self.add_asset_dialog = AssetFormPage(page, self)
#         # self.manage_asset_dialog = AssetFormManage(page, self)

#         self.add_asset_button = ft.ElevatedButton(
#             text="Add Asset",
#             icon=ft.Icons.ADD,
#             bgcolor=ft.Colors.TEAL_600,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=160,
#             height=50,
#             # on_click=lambda e: self.add_asset_dialog.open_dialog()
#         )

#         # Initialize table
#         self.data_table = ft.DataTable(
#             columns=[
#                 ft.DataColumn(ft.Text("Model")),
#                 ft.DataColumn(ft.Text("Serial")),
#                 ft.DataColumn(ft.Text("Location")),
#                 ft.DataColumn(ft.Text("Edit")),
#             ],
#             rows=[],
#             expand=True,
#             border=ft.border.all(1, ft.Colors.GREY_400),
#             vertical_lines=ft.border.BorderSide(1, ft.Colors.GREY_400),
#         )

#         # Load initial assets
#         self.load_assets()

#         self.content = ft.Container(
#             content=ft.Column(
#                 controls=[
#                     ft.Divider(height=1, color=ft.Colors.WHITE),
#                     ft.Row(
#                         controls=[
#                             ft.Text("Asset Management", size=24, weight=ft.FontWeight.BOLD, color="#263238"),
#                             self.add_asset_button
#                         ],
#                         alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#                     ),
#                     ft.Container(
#                         content=self.data_table,
#                         height=500,  # Adjusted for mobile screen
#                     ),
#                 ],
#                 expand=True,
#                 spacing=10,
#             ),
#             padding=10,  # Moved padding here
#         )

#         # Defer page update to ensure all controls are initialized
#         self.page.add(self)
#         self.page.update()

#     def load_assets(self):
#         """Reload asset data from the database and update the UI with available assets only."""
#         self.asset_add = []
#         db_config = {
#             "host": "200.200.200.23",
#             "user": "root",
#             "password": "Pak@123",
#             "database": "asm_sys",
#             "buffered": True
#         }

#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor_assets = conn.cursor(dictionary=True, buffered=True)
#             cursor_assets.execute("SELECT id, model, serial_number, location, status FROM assets")
#             assets = cursor_assets.fetchall()
#             print(f"Fetched {len(assets)} assets")
#             cursor_assets.close()

#             # Filter for available assets
#             available_assets = [asset for asset in assets if asset['status'].lower() == 'available']
#             self.asset_add = available_assets

#             conn.close()

#         except Error as e:
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Error fetching assets: {e}"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#             print(f"Error in load_assets: {e}")
#             self.page.update()
#         finally:
#             if 'cursor_assets' in locals():
#                 cursor_assets.close()
#             if 'conn' in locals():
#                 conn.close()

#         # Update table after loading assets
#         self.update_table()
#         self.page.update()

#     def update_table(self):
#         """Update the DataTable with available assets."""
#         rows = []
#         for asset in self.asset_add:
#             edit_button = ft.ElevatedButton(
#                 text="Edit",
#                 icon=ft.Icons.EDIT,
#                 bgcolor=ft.Colors.BLUE_300,
#                 color=ft.Colors.WHITE,
#                 width=60,
#                 on_click=lambda e, sn=asset['serial_number']: self.manage_asset_dialog.open(sn)
#             )
#             rows.append(
#                 ft.DataRow(
#                     cells=[
#                         ft.DataCell(ft.Text(asset['model'])),
#                         ft.DataCell(ft.Text(asset['serial_number'])),
#                         ft.DataCell(ft.Text(asset['location'])),
#                         ft.DataCell(ft.Container(content=edit_button, alignment=ft.alignment.center)),
#                     ]
#                 )
#             )
#         self.data_table.rows = rows

#     def close_asset_detail_dialog(self):
#         """Close the asset detail dialog (not used in this version)."""
#         if self.page.dialog:
#             self.page.dialog.open = False
#         self.page.update()

#     def update(self):
#         """Custom update method to ensure the control is updated."""
#         if self.page is not None:
#             self.page.update()

# if __name__ == "__main__":
#     ft.app(target=lambda page: AssetPage(page))

# import os
# os.environ["FLET_SECRET_KEY"] = "mysecret123"
# import flet as ft
# import mysql.connector
# from mysql.connector import Error
# import base64
# # from components.assetformpage import AssetFormPage
# # from components.assetformmanage import AssetFormManage

# class AssetPage(ft.Container):
#     def __init__(self, page: ft.Page):
#         super().__init__()

#         self.page = page
#         self.page.title = "Asset Management"
#         self.page.window_title = "Asset Management"
#         self.page.window.width = 400
#         self.page.window.height = 600
#         self.page.theme_mode = ft.ThemeMode.LIGHT  # Ensure light theme
#         self.page.bgcolor = ft.Colors.WHITE  # Prevent black background

#         self.expand = True
#         self.asset_add = []

#         # Initialize dialogs with self as parent (commented out as modules are not imported)
#         # self.add_asset_dialog = AssetFormPage(page, self)
#         # self.manage_asset_dialog = AssetFormManage(page, self)

#         self.add_asset_button = ft.ElevatedButton(
#             text="Add Asset",
#             icon=ft.Icons.ADD,
#             bgcolor=ft.Colors.TEAL_600,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=160,
#             height=50,
#             # on_click=lambda e: self.add_asset_dialog.open_dialog()  # Commented out due to missing module
#         )

#         # Initialize table
#         self.data_table = ft.DataTable(
#             columns=[
#                 ft.DataColumn(ft.Text("Model")),
#                 ft.DataColumn(ft.Text("Serial")),
#                 ft.DataColumn(ft.Text("Location")),
#                 ft.DataColumn(ft.Text("Edit")),
#             ],
#             rows=[],
#             border=ft.border.all(1, ft.Colors.GREY_400),
#             vertical_lines=ft.border.BorderSide(1, ft.Colors.GREY_400),
#             column_spacing=5,
#         )

#         # Load initial assets
#         self.load_assets()

#         self.content = ft.Container(
#             content=ft.Column(
#                 controls=[
#                     ft.Divider(height=1, color=ft.Colors.WHITE),
#                     ft.Row(
#                         controls=[
                          
#                             self.add_asset_button
#                         ],
#                         alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#                     ),
#                     ft.Container(
#                         content=self.data_table,
#                         expand=True,  # Expand to fill available height
#                         width=self.page.window.width - 20,  # Adjust for padding
#                         clip_behavior=ft.ClipBehavior.HARD_EDGE,
#                         padding=5,
#                         border=ft.border.all(1, ft.Colors.GREY_400),
#                     ),
#                 ],
#                 expand=True,  # Ensure column fills the window
#                 spacing=10,
#             ),
#             padding=10,  # 10px padding on each side, total 20px subtracted from width
#         )

#         # Defer page update to ensure all controls are initialized
#         self.page.add(self)
#         self.page.update()

#     def load_assets(self):
#         """Reload asset data from the database and update the UI with available assets only."""
#         self.asset_add = []
#         db_config = {
#             "host": "200.200.200.23",
#             "user": "root",
#             "password": "Pak@123",
#             "database": "asm_sys",
#             "buffered": True
#         }

#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor_assets = conn.cursor(dictionary=True, buffered=True)
#             cursor_assets.execute("SELECT id, model, serial_number, location, status FROM assets")
#             assets = cursor_assets.fetchall()
#             print(f"Fetched {len(assets)} assets")
#             cursor_assets.close()

#             # Filter for available assets
#             available_assets = [asset for asset in assets if asset['status'].lower() == 'available']
#             self.asset_add = available_assets
#             print(f"Available assets: {len(self.asset_add)}")  # Debug print

#             conn.close()

#         except Error as e:
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Error fetching assets: {e}"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#             print(f"Error in load_assets: {e}")
#             self.page.update()
#         finally:
#             if 'cursor_assets' in locals():
#                 cursor_assets.close()
#             if 'conn' in locals():
#                 conn.close()

#         # Update table after loading assets
#         self.update_table()
#         self.page.update()

#     def update_table(self):
#         """Update the DataTable with available assets."""
#         rows = []
#         print(f"Updating table with {len(self.asset_add)} rows")  # Debug print
#         for asset in self.asset_add:
#             edit_button = ft.IconButton(
#                 icon=ft.Icons.EDIT,
#             )
#             rows.append(
#                 ft.DataRow(
#                     cells=[
#                         ft.DataCell(ft.Text(asset['model'])),
#                         ft.DataCell(ft.Text(asset['serial_number'])),
#                         ft.DataCell(ft.Text(asset['location'])),
#                         ft.DataCell(ft.Container(content=edit_button, alignment=ft.alignment.center)),
#                     ]
#                 )
#             )
#         self.data_table.rows = rows
#         print(f"Table rows updated: {len(rows)}")  # Debug print

#     def close_asset_detail_dialog(self):
#         """Close the asset detail dialog (not used in this version)."""
#         if self.page.dialog:
#             self.page.dialog.open = False
#         self.page.update()

#     def update(self):
#         """Custom update method to ensure the control is updated."""
#         if self.page is not None:
#             self.page.update()

# if __name__ == "__main__":
#     ft.app(target=lambda page: AssetPage(page))


# import os
# os.environ["FLET_SECRET_KEY"] = "mysecret123"
# import flet as ft
# import mysql.connector
# from mysql.connector import Error
# import base64
# from assetpage import AssetFormPage
# import sqlite3
# # from components.assetformpage import AssetFormPage
# # from components.assetformmanage import AssetFormManage

# class AssetPage(ft.Container):
#     def __init__(self, page: ft.Page):
#         super().__init__()

#         self.page = page
#         self.page.title = "Asset Management"
    
#         self.page.window.width = 365
#         self.page.window.height = 600
#         self.page.window.min_width = 360  # Enforce minimum width
#         self.page.window.min_height = 600  # Enforce minimum height
#         # self.page.window.width = 320
#         # self.page.window.height = 600
#         self.page.theme_mode = ft.ThemeMode.LIGHT  # Ensure light theme
#         self.page.bgcolor = ft.Colors.WHITE  # Prevent black background


#         self.local_db = sqlite3.connect("assets.db", check_same_thread=False)
#         self.initialize_local_db()
        
#         self.add_asset_dialog = AssetFormPage(self.page, self, local_db=self.local_db)
        
#         # Set up AppBar
#         self.page.appbar = ft.AppBar(
#             title=ft.Text("Asset Management", size=15, weight="bold"),
#             bgcolor=ft.Colors.GREEN_300,
#             color=ft.Colors.WHITE,
#             center_title=True,
#             automatically_imply_leading=False,
#         )

#         # Set up BottomAppBar
#         self.page.bottom_appbar = ft.BottomAppBar(
#             bgcolor=ft.Colors.BLUE,
#             shape=ft.NotchShape.CIRCULAR,
#             content=ft.Row(
#                 controls=[
#                     ft.PopupMenuButton(
#                         items=[
#                             ft.PopupMenuItem(text="Option 1"),
#                             ft.PopupMenuItem(text="Option 2"),
#                             ft.PopupMenuItem(text="Option 3"),
#                             ft.PopupMenuItem(text="Option 4"),
#                         ],
#                         icon=ft.Icon(ft.Icons.MENU_BOOK, color=ft.Colors.WHITE),
#                         tooltip="Menu Options",
#                     ),
#                     ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE, tooltip="Search"),
#                     ft.Container(expand=True),  # Spacer
#                     ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE, tooltip="Favorites"),
#                 ],
#             ),
#         )

#         self.expand = True
#         self.asset_add = []

#         # Initialize dialogs with self as parent (commented out as modules are not imported)
#         # self.add_asset_dialog = AssetFormPage(page, self)
#         # self.manage_asset_dialog = AssetFormManage(page, self)

#         self.add_asset_button = ft.ElevatedButton(
#             text="Add Asset",
#             icon=ft.Icons.ADD,
#             bgcolor=ft.Colors.TEAL_600,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#             # on_click=lambda e: self.add_asset_dialog.open_dialog()  # Commented out due to missing module
#         )

#         # Initialize table
#         self.data_table = ft.DataTable(
#             columns=[
#                 ft.DataColumn(ft.Text("Model", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Serial", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Location", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Edit", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#             ],
#             rows=[],
#             border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#             vertical_lines=ft.border.BorderSide(1, ft.Colors.BLUE_GREY_300),
#             column_spacing=5,
#         )

#         # Load initial assets
#         self.load_assets()

#         self.content = ft.Container(
#             content=ft.Column(
#                 controls=[
#                     ft.Row(
#                         controls=[
                    
#                             self.add_asset_button
#                         ],
#                         alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#                     ),
#                     ft.Container(
#                         content=self.data_table,
#                         expand=True,  # Expand to fill available height
#                         width=self.page.window.width - 20,  # Adjust for padding
#                         clip_behavior=ft.ClipBehavior.HARD_EDGE,
#                         padding=5,
#                         border_radius=10,
#                         bgcolor=ft.Colors.LIGHT_BLUE_100,  # Colored table background
#                         border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#                     ),
#                 ],
#                 expand=True,  # Ensure column fills the window
#                 spacing=10,
#                 scroll=ft.ScrollMode.AUTO,  # Enable scrolling for the column
#             ),
#             padding=10, 
            
#              # 10px padding on each side, total 20px subtracted from width
#         )

#         # Defer page update to ensure all controls are initialized
#         self.page.add(self)
#         self.page.update()

#     def load_assets(self):
#         """Reload asset data from the database and update the UI with available assets only."""
#         self.asset_add = []
#         db_config = {
#             "host": "200.200.200.23",
#             "user": "root",
#             "password": "Pak@123",
#             "database": "asm_sys",
#             "buffered": True
#         }

#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor_assets = conn.cursor(dictionary=True, buffered=True)
#             cursor_assets.execute("SELECT id, model, serial_number, location, status FROM assets")
#             assets = cursor_assets.fetchall()
#             print(f"Fetched {len(assets)} assets")
#             cursor_assets.close()

#             # Filter for available assets
#             available_assets = [asset for asset in assets if asset['status'].lower() == 'available']
#             self.asset_add = available_assets
#             print(f"Available assets: {len(self.asset_add)}")  # Debug print

#             conn.close()

#         except Error as e:
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Error fetching assets: {e}"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#             print(f"Error in load_assets: {e}")
#             self.page.update()
#         finally:
#             if 'cursor_assets' in locals():
#                 cursor_assets.close()
#             if 'conn' in locals():
#                 conn.close()

#         # Update table after loading assets
#         self.update_table()
#         self.page.update()

#     def update_table(self):
#         """Update the DataTable with available assets."""
#         rows = []
#         print(f"Updating table with {len(self.asset_add)} rows")  # Debug print
#         for i, asset in enumerate(self.asset_add):
#             edit_button = ft.IconButton(
#                 icon=ft.Icons.EDIT,
#                 icon_color=ft.Colors.BLUE,
#                 bgcolor=ft.LinearGradient(
#                     begin=ft.alignment.top_left,
#                     end=ft.alignment.bottom_right,
#                     colors=[ft.Colors.BLUE_500, ft.Colors.BLUE_700]
#                 ),
#                 style=ft.ButtonStyle(
#                     shape=ft.RoundedRectangleBorder(radius=8),
#                     overlay_color=ft.Colors.BLUE_400
#                 ),
#                 tooltip="Edit Asset"
#             )
#             rows.append(
#                 ft.DataRow(
#                     cells=[
#                         ft.DataCell(ft.Text(asset['model'], color=ft.Colors.BLUE_GREY_800, size=12)),
#                         ft.DataCell(ft.Text(asset['serial_number'], color=ft.Colors.BLUE_GREY_800, size=12)),
#                         ft.DataCell(ft.Text(asset['location'], color=ft.Colors.BLUE_GREY_800, size=12)),
#                         ft.DataCell(ft.Container(content=edit_button, alignment=ft.alignment.center)),
#                     ],
#                     color=ft.Colors.WHITE if i % 2 == 0 else ft.Colors.BLUE_GREY_50  # Alternating row colors
#                 )
#             )
#         self.data_table.rows = rows
#         print(f"Table rows updated: {len(rows)}")  # Debug print

#     def close_asset_detail_dialog(self):
#         """Close the asset detail dialog (not used in this version)."""
#         if self.page.dialog:
#             self.page.dialog.open = False
#         self.page.update()

#     def update(self):
#         """Custom update method to ensure the control is updated."""
#         if self.page is not None:
#             self.page.update()



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


# import os
# os.environ["FLET_SECRET_KEY"] = "mysecret123"
# import flet as ft
# import mysql.connector
# from mysql.connector import Error
# import base64
# from assetpage import AssetFormPage
# from assetedit import AssetEditPage
# import sqlite3

# class AssetPage(ft.Container):
#     def __init__(self, page: ft.Page):
#         super().__init__()

#         self.page = page
#         self.page.title = "Asset Management"
    
#         self.page.window.width = 365
#         self.page.window.height = 600
#         self.page.window.min_width = 360  # Enforce minimum width
#         self.page.window.min_height = 600  # Enforce minimum height
#         self.page.theme_mode = ft.ThemeMode.LIGHT  # Ensure light theme
#         self.page.bgcolor = ft.Colors.WHITE  # Prevent black background

#         self.local_db = sqlite3.connect("assets.db", check_same_thread=False)
#         self.initialize_local_db()
        
#         self.add_asset_dialog = AssetFormPage(self.page, self, local_db=self.local_db)
        
#         # Set up AppBar
#         self.page.appbar = ft.AppBar(
#             title=ft.Text("Asset Management", size=15, weight="bold"),
#             bgcolor=ft.Colors.GREEN_300,
#             color=ft.Colors.WHITE,
#             center_title=True,
#             automatically_imply_leading=False,
#         )

#         # Set up BottomAppBar
#         self.page.bottom_appbar = ft.BottomAppBar(
#             bgcolor=ft.Colors.BLUE,
#             shape=ft.NotchShape.CIRCULAR,
#             content=ft.Row(
#                 controls=[
#                     ft.PopupMenuButton(
#                         items=[
#                             ft.PopupMenuItem(text="Option 1"),
#                             ft.PopupMenuItem(text="Option 2"),
#                             ft.PopupMenuItem(text="Option 3"),
#                             ft.PopupMenuItem(text="Option 4"),
#                         ],
#                         icon=ft.Icon(ft.Icons.MENU_BOOK, color=ft.Colors.WHITE),
#                         tooltip="Menu Options",
#                     ),
#                     ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE, tooltip="Search"),
#                     ft.Container(expand=True),  # Spacer
#                     ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE, tooltip="Favorites"),
#                 ],
#             ),
#         )

#         self.expand = True
#         self.asset_add = []

#         self.add_asset_button = ft.ElevatedButton(
#             text="Add Asset",
#             icon=ft.Icons.ADD,
#             bgcolor=ft.Colors.TEAL_600,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#         )

#         # Initialize table
#         self.data_table = ft.DataTable(
#             columns=[
#                 ft.DataColumn(ft.Text("Model", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Serial", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Location", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Edit", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#             ],
#             rows=[],
#             border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#             vertical_lines=ft.border.BorderSide(1, ft.Colors.BLUE_GREY_300),
#             column_spacing=5,
#         )

#         # Load initial assets
#         self.load_assets()

#         self.content = ft.Container(
#             content=ft.Column(
#                 controls=[
#                     ft.Row(
#                         controls=[self.add_asset_button],
#                         alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#                     ),
#                     ft.Container(
#                         content=self.data_table,
#                         expand=True,  # Expand to fill available height
#                         width=self.page.window.width - 20,  # Adjust for padding
#                         clip_behavior=ft.ClipBehavior.HARD_EDGE,
#                         padding=5,
#                         border_radius=10,
#                         bgcolor=ft.Colors.LIGHT_BLUE_100,  # Colored table background
#                         border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#                     ),
#                 ],
#                 expand=True,  # Ensure column fills the window
#                 spacing=10,
#                 scroll=ft.ScrollMode.AUTO,  # Enable scrolling for the column
#             ),
#             padding=10,
#         )

#         # Defer page update to ensure all controls are initialized
#         self.page.add(self)
#         self.page.update()

#     def load_assets(self):
#         """Reload asset data from the database and update the UI with available assets only."""
#         self.asset_add = []
#         db_config = {
#             "host": "200.200.200.23",
#             "user": "root",
#             "password": "Pak@123",
#             "database": "asm_sys",
#             "buffered": True
#         }

#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor_assets = conn.cursor(dictionary=True, buffered=True)
#             cursor_assets.execute("SELECT id, model, serial_number, location, status FROM assets")
#             assets = cursor_assets.fetchall()
#             print(f"Fetched {len(assets)} assets")
#             cursor_assets.close()

#             # Filter for available assets
#             available_assets = [asset for asset in assets if asset['status'].lower() == 'available']
#             self.asset_add = available_assets
#             print(f"Available assets: {len(self.asset_add)}")  # Debug print

#             conn.close()

#         except Error as e:
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Error fetching assets: {e}"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#             print(f"Error in load_assets: {e}")
#             self.page.update()
#         finally:
#             if 'cursor_assets' in locals():
#                 cursor_assets.close()
#             if 'conn' in locals():
#                 conn.close()

#         # Update table after loading assets
#         self.update_table()
#         self.page.update()

#     def update_table(self):
#         """Update the DataTable with available assets."""
#         rows = []
#         print(f"Updating table with {len(self.asset_add)} rows")  # Debug print
#         for i, asset in enumerate(self.asset_add):
#             edit_button = ft.IconButton(
#                 icon=ft.Icons.EDIT,
#                 icon_color=ft.Colors.BLUE,
#                 bgcolor=ft.LinearGradient(
#                     begin=ft.alignment.top_left,
#                     end=ft.alignment.bottom_right,
#                     colors=[ft.Colors.BLUE_500, ft.Colors.BLUE_700]
#                 ),
#                 style=ft.ButtonStyle(
#                     shape=ft.RoundedRectangleBorder(radius=8),
#                     overlay_color=ft.Colors.BLUE_400
#                 ),
#                 tooltip="Edit Asset",
#                 on_click=lambda e, aid=asset['id']: self.open_edit_dialog(aid)
#             )
#             rows.append(
#                 ft.DataRow(
#                     cells=[
#                         ft.DataCell(ft.Text(asset['model'], color=ft.Colors.BLUE_GREY_800, size=12)),
#                         ft.DataCell(ft.Text(asset['serial_number'], color=ft.Colors.BLUE_GREY_800, size=12)),
#                         ft.DataCell(ft.Text(asset['location'], color=ft.Colors.BLUE_GREY_800, size=12)),
#                         ft.DataCell(ft.Container(content=edit_button, alignment=ft.alignment.center)),
#                     ],
#                     color=ft.Colors.WHITE if i % 2 == 0 else ft.Colors.BLUE_GREY_50  # Alternating row colors
#                 )
#             )
#         self.data_table.rows = rows
#         print(f"Table rows updated: {len(rows)}")  # Debug print

#     def open_edit_dialog(self, asset_id):
#         """Open the edit dialog for the specified asset."""
#         self.edit_dialog = AssetEditPage(self.page, self, asset_id=asset_id, local_db=self.local_db)
#         self.edit_dialog.open_dialog()

#     def close_asset_detail_dialog(self):
#         """Close the asset detail dialog (not used in this version)."""
#         if self.page.dialog:
#             self.page.dialog.open = False
#         self.page.update()

#     def update(self):
#         """Custom update method to ensure the control is updated."""
#         if self.page is not None:
#             self.page.update()

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


# import os
# os.environ["FLET_SECRET_KEY"] = "mysecret123"
# import flet as ft
# import mysql.connector
# from mysql.connector import Error
# import base64
# from assetpage import AssetFormPage
# from assetedit import AssetEditPage
# import sqlite3

# class AssetPage(ft.Container):
#     def __init__(self, page: ft.Page):
#         super().__init__()

#         self.page = page
#         self.page.title = "Asset Management"
    
#         self.page.window.width = 365
#         self.page.window.height = 600
#         self.page.window.min_width = 360  # Enforce minimum width
#         self.page.window.min_height = 600  # Enforce minimum height
#         self.page.theme_mode = ft.ThemeMode.LIGHT  # Ensure light theme
#         self.page.bgcolor = ft.Colors.WHITE  # Prevent black background

#         self.local_db = sqlite3.connect("assets.db", check_same_thread=False)
#         self.initialize_local_db()
        
#         self.add_asset_dialog = AssetFormPage(self.page, self, local_db=self.local_db)
        
#         # Set up AppBar
#         self.page.appbar = ft.AppBar(
#             title=ft.Text("Asset Management", size=15, weight="bold"),
#             bgcolor=ft.Colors.GREEN_300,
#             color=ft.Colors.WHITE,
#             center_title=True,
#             automatically_imply_leading=False,
#         )

#         # Set up BottomAppBar
#         self.page.bottom_appbar = ft.BottomAppBar(
#             bgcolor=ft.Colors.BLUE,
#             shape=ft.NotchShape.CIRCULAR,
#             content=ft.Row(
#                 controls=[
#                     ft.PopupMenuButton(
#                         items=[
#                             ft.PopupMenuItem(text="Option 1"),
#                             ft.PopupMenuItem(text="Option 2"),
#                             ft.PopupMenuItem(text="Option 3"),
#                             ft.PopupMenuItem(text="Option 4"),
#                         ],
#                         icon=ft.Icon(ft.Icons.MENU_BOOK, color=ft.Colors.WHITE),
#                         tooltip="Menu Options",
#                     ),
#                     ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE, tooltip="Search"),
#                     ft.Container(expand=True),  # Spacer
#                     ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE, tooltip="Favorites"),
#                 ],
#             ),
#         )

#         self.expand = True
#         self.asset_add = []

#         self.add_asset_button = ft.ElevatedButton(
#             text="Add Asset",
#             icon=ft.Icons.ADD,
#             bgcolor=ft.Colors.TEAL_600,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#         )

#         self.Home_button = ft.ElevatedButton(
#             text="HOME",
#             icon=ft.Icons.HOME,
#             bgcolor=ft.Colors.GREEN_400,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.page.go("/"),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#         )

#         # Initialize table
#         self.data_table = ft.DataTable(
#             columns=[
#                 ft.DataColumn(ft.Text("Model", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Serial", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Location", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Edit", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#             ],
#             rows=[],
#             border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#             vertical_lines=ft.border.BorderSide(1, ft.Colors.BLUE_GREY_300),
#             column_spacing=5,
#         )

#         # Load initial assets
#         self.load_assets()

#         self.content = ft.Container(
#             content=ft.Column(
#                 controls=[
#                     ft.Row(
#                         controls=[self.Home_button,self.add_asset_button],
#                         alignment=ft.MainAxisAlignment.START,
#                         spacing=10,
#                     ),
#                     ft.Container(
#                         content=self.data_table,
#                         expand=True,  # Expand to fill available height
#                         width=self.page.window.width - 20,  # Adjust for padding
#                         clip_behavior=ft.ClipBehavior.HARD_EDGE,
#                         padding=5,
#                         border_radius=10,
#                         bgcolor=ft.Colors.LIGHT_BLUE_100,  # Colored table background
#                         border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#                     ),
#                 ],
#                 expand=True,  # Ensure column fills the window
#                 spacing=10,
#                 scroll=ft.ScrollMode.AUTO,  # Enable scrolling for the column
#             ),
#             padding=10,
#         )

#         # Defer page update to ensure all controls are initialized
#         self.page.add(self)
#         self.page.update()

#     def load_assets(self):
#         """Reload asset data from the database and update the UI with available assets only."""
#         self.asset_add = []
#         db_config = {
#             "host": "200.200.200.23",
#             "user": "root",
#             "password": "Pak@123",
#             "database": "asm_sys",
#             "buffered": True
#         }

#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor_assets = conn.cursor(dictionary=True, buffered=True)
#             cursor_assets.execute("SELECT id, model, serial_number, location, status FROM assets")
#             assets = cursor_assets.fetchall()
#             print(f"Fetched {len(assets)} assets")
#             cursor_assets.close()

#             # Filter for available assets
#             available_assets = [asset for asset in assets if asset['status'].lower() == 'available']
#             self.asset_add = available_assets
#             print(f"Available assets: {len(self.asset_add)}")  # Debug print

#             conn.close()

#         except Error as e:
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Error fetching assets: {e}"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#             print(f"Error in load_assets: {e}")
#             self.page.update()
#         finally:
#             if 'cursor_assets' in locals():
#                 cursor_assets.close()
#             if 'conn' in locals():
#                 conn.close()

#         # Update table after loading assets
#         self.update_table()
#         self.page.update()

#     def update_table(self):
#         """Update the DataTable with available assets."""
#         rows = []
#         print(f"Updating table with {len(self.asset_add)} rows")  # Debug print
#         for i, asset in enumerate(self.asset_add):
#             edit_button = ft.IconButton(
#                 icon=ft.Icons.EDIT,
#                 icon_color=ft.Colors.BLUE,
#                 bgcolor=ft.LinearGradient(
#                     begin=ft.alignment.top_left,
#                     end=ft.alignment.bottom_right,
#                     colors=[ft.Colors.BLUE_500, ft.Colors.BLUE_700]
#                 ),
#                 style=ft.ButtonStyle(
#                     shape=ft.RoundedRectangleBorder(radius=8),
#                     overlay_color=ft.Colors.BLUE_400
#                 ),
#                 tooltip="Edit Asset",
#                 on_click=lambda e, aid=asset['id']: self.open_edit_dialog(aid)
#             )
#             rows.append(
#                 ft.DataRow(
#                     cells=[
#                         ft.DataCell(ft.Text(asset['model'], color=ft.Colors.BLUE_GREY_800, size=12)),
#                         ft.DataCell(ft.Text(asset['serial_number'], color=ft.Colors.BLUE_GREY_800, size=12)),
#                         ft.DataCell(ft.Text(asset['location'], color=ft.Colors.BLUE_GREY_800, size=12)),
#                         ft.DataCell(ft.Container(content=edit_button, alignment=ft.alignment.center)),
#                     ],
#                     color=ft.Colors.WHITE if i % 2 == 0 else ft.Colors.BLUE_GREY_50  # Alternating row colors
#                 )
#             )
#         self.data_table.rows = rows
#         print(f"Table rows updated: {len(rows)}")  # Debug print

#     def open_edit_dialog(self, asset_id):
#         """Open the edit dialog for the specified asset."""
#         self.edit_dialog = AssetEditPage(self.page, self, asset_id=asset_id, local_db=self.local_db)
#         self.edit_dialog.open_dialog()

#     def close_asset_detail_dialog(self):
#         """Close the asset detail dialog (not used in this version)."""
#         if self.page.dialog:
#             self.page.dialog.open = False
#         self.page.update()

#     def update(self):
#         """Custom update method to ensure the control is updated."""
#         if self.page is not None:
#             self.page.update()

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



# import os
# os.environ["FLET_SECRET_KEY"] = "mysecret123"
# import flet as ft
# import mysql.connector
# from mysql.connector import Error
# import sqlite3
# from assetpage import AssetFormPage
# from assetedit import AssetEditPage
# import time

# class AssetPage(ft.Container):
#     def __init__(self, page: ft.Page):
#         super().__init__()

#         self.page = page
#         self.page.title = "Asset Management"
    
#         self.page.window.width = 365
#         self.page.window.height = 600
#         self.page.window.min_width = 360
#         self.page.window.min_height = 600
#         self.page.theme_mode = ft.ThemeMode.LIGHT
#         self.page.bgcolor = ft.Colors.WHITE

#         self.local_db = sqlite3.connect("assets.db", check_same_thread=False)
#         self.initialize_local_db()
        
#         self.add_asset_dialog = AssetFormPage(self.page, self, local_db=self.local_db)
        
#         self.page.appbar = ft.AppBar(
#             title=ft.Text("Asset Management", size=15, weight="bold"),
#             bgcolor=ft.Colors.GREEN_300,
#             color=ft.Colors.WHITE,
#             center_title=True,
#             automatically_imply_leading=False,
#         )

#         self.page.bottom_appbar = ft.BottomAppBar(
#             bgcolor=ft.Colors.BLUE,
#             shape=ft.NotchShape.CIRCULAR,
#             content=ft.Row(
#                 controls=[
#                     ft.PopupMenuButton(
#                         items=[
#                             ft.PopupMenuItem(text="Option 1"),
#                             ft.PopupMenuItem(text="Option 2"),
#                             ft.PopupMenuItem(text="Option 3"),
#                             ft.PopupMenuItem(text="Option 4"),
#                         ],
#                         icon=ft.Icon(ft.Icons.MENU_BOOK, color=ft.Colors.WHITE),
#                         tooltip="Menu Options",
#                     ),
#                     ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE, tooltip="Search"),
#                     ft.Container(expand=True),
#                     ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE, tooltip="Favorites"),
#                 ],
#             ),
#         )

#         self.expand = True
#         self.asset_add = []

#         self.add_asset_button = ft.ElevatedButton(
#             text="Add Asset",
#             icon=ft.Icons.ADD,
#             bgcolor=ft.Colors.TEAL_600,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#         )

#         self.Home_button = ft.ElevatedButton(
#             text="HOME",
#             icon=ft.Icons.HOME,
#             bgcolor=ft.Colors.GREEN_400,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.page.go("/"),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#         )

#         # Initialize local asset table
#         self.local_asset_table = ft.DataTable(
#             columns=[
#                 ft.DataColumn(ft.Text("ID")),
#                 ft.DataColumn(ft.Text("Model")),
#                 ft.DataColumn(ft.Text("Serial Number")),
#                 ft.DataColumn(ft.Text("Company")),
#                 ft.DataColumn(ft.Text("Location")),
#                 ft.DataColumn(ft.Text("Purchase Date")),
#                 ft.DataColumn(ft.Text("Status")),
#                 ft.DataColumn(ft.Text("Last Sync")),
#             ],
#             rows=[],
#         )

#         self.sync_from_server_button = ft.ElevatedButton(
#             text="Sync from Server",
#             icon=ft.Icons.DOWNLOAD,
#             bgcolor=ft.Colors.PURPLE_500,
#             color=ft.Colors.WHITE,
#             on_click=self.sync_from_server,
#             width=150,
#             height=40,
#         )

#         self.sync_to_server_button = ft.ElevatedButton(
#             text="Sync to Server",
#             icon=ft.Icons.UPLOAD,
#             bgcolor=ft.Colors.PINK_500,
#             color=ft.Colors.WHITE,
#             on_click=self.sync_to_server,
#             width=150,
#             height=40,
#         )

#         self.content = ft.Container(
#             content=ft.Column(
#                 controls=[
#                     ft.Row(
#                         controls=[self.Home_button, self.add_asset_button],
#                         alignment=ft.MainAxisAlignment.START,
#                         spacing=10,
#                     ),
#                     ft.Text("Local Assets", size=18, weight=ft.FontWeight.BOLD),
#                     ft.Container(
#                         content=self.local_asset_table,
#                         expand=True,
#                         width=self.page.window.width - 20,
#                         clip_behavior=ft.ClipBehavior.HARD_EDGE,
#                         padding=5,
#                         border_radius=10,
#                         bgcolor=ft.Colors.LIGHT_BLUE_100,
#                         border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#                     ),
#                     ft.Row(
#                         controls=[self.sync_from_server_button, self.sync_to_server_button],
#                         alignment=ft.MainAxisAlignment.CENTER,
#                         spacing=10,
#                     ),
#                 ],
#                 expand=True,
#                 spacing=10,
#                 scroll=ft.ScrollMode.AUTO,
#             ),
#             padding=10,
#         )

#         # Load initial local assets
#         self.refresh_local_assets()
#         self.page.add(self)
#         self.page.update()

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

#     def refresh_local_assets(self):
#         cursor = self.local_db.cursor()
#         try:
#             cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status, last_sync FROM assets")
#             assets = cursor.fetchall()
#             print(f"SQLite3 query returned {len(assets)} assets: {[row[2] for row in assets]}")

#             self.local_asset_table.rows.clear()

#             if not assets:
#                 self.local_asset_table.rows.append(
#                     ft.DataRow(
#                         cells=[
#                             ft.DataCell(ft.Text("No local assets found in SQLite3.")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                         ]
#                     )
#                 )
#             else:
#                 for asset in assets:
#                     asset_id, model, serial_number, company, location, purchase_date, status, last_sync = asset
#                     self.local_asset_table.rows.append(
#                         ft.DataRow(
#                             cells=[
#                                 ft.DataCell(ft.Text(str(asset_id))),
#                                 ft.DataCell(ft.Text(model or "N/A")),
#                                 ft.DataCell(ft.Text(serial_number or "N/A")),
#                                 ft.DataCell(ft.Text(company or "N/A")),
#                                 ft.DataCell(ft.Text(location or "N/A")),
#                                 ft.DataCell(ft.Text(purchase_date or "N/A")),
#                                 ft.DataCell(ft.Text(status or "N/A")),
#                                 ft.DataCell(ft.Text(last_sync or "N/A")),
#                             ]
#                         )
#                     )

#             self.page.update()
#         except Exception as e:
#             print(f"Error fetching local asset data from SQLite3: {e}")
#             self.local_asset_table.rows.clear()
#             self.local_asset_table.rows.append(
#                 ft.DataRow(
#                     cells=[
#                         ft.DataCell(ft.Text(f"Error: {e}")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                     ]
#                 )
#             )
#             self.page.update()
#         finally:
#             cursor.close()

#     def sync_from_server(self, e):
#         db_config = {"host": "200.200.200.23", "user": "root", "password": "Pak@123", "database": "asm_sys"}
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             local_cursor = self.local_db.cursor()

#             local_cursor.execute("BEGIN TRANSACTION")
#             cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status FROM assets")
#             mysql_assets = cursor.fetchall()

#             for asset in mysql_assets:
#                 mysql_id, model, serial_number, company, location, purchase_date, status = asset
#                 local_cursor.execute("SELECT id FROM assets WHERE serial_number = ?", (serial_number,))
#                 existing_asset = local_cursor.fetchone()
#                 if existing_asset:
#                     local_id = existing_asset[0]
#                     local_cursor.execute("""
#                         UPDATE assets SET model = ?, company = ?, location = ?, purchase_date = ?, status = ?, last_sync = ?
#                         WHERE id = ?
#                     """, (model, company, location, purchase_date, status, time.strftime("%Y-%m-%d %H:%M:%S"), local_id))
#                 else:
#                     local_cursor.execute("""
#                         INSERT INTO assets (model, serial_number, company, location, purchase_date, status, last_sync)
#                         VALUES (?, ?, ?, ?, ?, ?, ?)
#                     """, (model, serial_number, company, location, purchase_date, status, time.strftime("%Y-%m-%d %H:%M:%S")))

#                 cursor.execute("SELECT id, asset_id, image_name, image_data FROM asset_images WHERE asset_id = %s", (mysql_id,))
#                 mysql_images = cursor.fetchall()
#                 local_cursor.execute("SELECT id, image_name FROM asset_images WHERE asset_id = (SELECT id FROM assets WHERE serial_number = ?)", (serial_number,))
#                 existing_images = {row[1]: row[0] for row in local_cursor.fetchall()}
#                 for img in mysql_images:
#                     img_id, asset_id, image_name, image_data = img
#                     if image_name in existing_images:
#                         local_cursor.execute("""
#                             UPDATE asset_images SET image_data = ?, last_sync = ? WHERE id = ?
#                         """, (image_data, time.strftime("%Y-%m-%d %H:%M:%S"), existing_images[image_name]))
#                     else:
#                         local_cursor.execute("""
#                             INSERT INTO asset_images (asset_id, image_name, image_data, last_sync)
#                             VALUES ((SELECT id FROM assets WHERE serial_number = ?), ?, ?, ?)
#                         """, (serial_number, image_name, image_data, time.strftime("%Y-%m-%d %H:%M:%S")))

#                 cursor.execute("SELECT id, asset_id, bill_name, bill_data FROM asset_bills WHERE asset_id = %s", (mysql_id,))
#                 mysql_bills = cursor.fetchall()
#                 local_cursor.execute("SELECT id, bill_name FROM asset_bills WHERE asset_id = (SELECT id FROM assets WHERE serial_number = ?)", (serial_number,))
#                 existing_bills = {row[1]: row[0] for row in cursor.fetchall()}
#                 for bill in mysql_bills:
#                     bill_id, asset_id, bill_name, bill_data = bill
#                     if bill_name in existing_bills:
#                         local_cursor.execute("""
#                             UPDATE asset_bills SET bill_data = ?, last_sync = ? WHERE id = ?
#                         """, (bill_data, time.strftime("%Y-%m-%d %H:%M:%S"), existing_bills[bill_name]))
#                     else:
#                         local_cursor.execute("""
#                             INSERT INTO asset_bills (asset_id, bill_name, bill_data, last_sync)
#                             VALUES ((SELECT id FROM assets WHERE serial_number = ?), ?, ?, ?)
#                         """, (serial_number, bill_name, bill_data, time.strftime("%Y-%m-%d %H:%M:%S")))

#             self.local_db.commit()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text("Sync from server completed!"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#             self.refresh_local_assets()
#         except Error as e:
#             self.local_db.rollback()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Sync error: {e}"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#         finally:
#             if 'cursor' in locals():
#                 cursor.close()
#             if 'conn' in locals():
#                 conn.close()
#             if 'local_cursor' in locals():
#                 local_cursor.close()
#             self.page.update()

#     def sync_to_server(self, e):
#         db_config = {"host": "200.200.200.23", "user": "root", "password": "Pak@123", "database": "asm_sys"}
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             local_cursor = self.local_db.cursor()

#             cursor.execute("BEGIN")
#             local_cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status, last_sync FROM assets")
#             local_assets = local_cursor.fetchall()

#             for asset in local_assets:
#                 local_id, model, serial_number, company, location, purchase_date, status, last_sync = asset
#                 cursor.execute("SELECT id FROM assets WHERE serial_number = %s", (serial_number,))
#                 existing_asset = cursor.fetchone()
#                 if existing_asset:
#                     mysql_id = existing_asset[0]
#                     cursor.execute("""
#                         UPDATE assets SET model = %s, company = %s, location = %s, purchase_date = %s, status = %s
#                         WHERE id = %s
#                     """, (model, company, location, purchase_date, status, mysql_id))
#                 else:
#                     cursor.execute("""
#                         INSERT INTO assets (model, serial_number, company, location, purchase_date, status)
#                         VALUES (%s, %s, %s, %s, %s, %s)
#                     """, (model, serial_number, company, location, purchase_date, status))
#                     mysql_id = cursor.lastrowid

#                 local_cursor.execute("SELECT id, asset_id, image_name, image_data, last_sync FROM asset_images WHERE asset_id = ?", (local_id,))
#                 images = local_cursor.fetchall()
#                 cursor.execute("SELECT id, image_name FROM asset_images WHERE asset_id = %s", (mysql_id,))
#                 existing_images = {row[0]: row[1] for row in cursor.fetchall()}
#                 for img in images:
#                     img_id, asset_id, image_name, image_data, last_sync = img
#                     if img_id in existing_images:
#                         cursor.execute("""
#                             UPDATE asset_images SET image_name = %s, image_data = %s WHERE id = %s AND asset_id = %s
#                         """, (image_name, image_data, img_id, mysql_id))
#                     else:
#                         cursor.execute("""
#                             INSERT INTO asset_images (asset_id, image_name, image_data)
#                             VALUES (%s, %s, %s)
#                         """, (mysql_id, image_name, image_data))

#                 local_cursor.execute("SELECT id, asset_id, bill_name, bill_data, last_sync FROM asset_bills WHERE asset_id = ?", (local_id,))
#                 bills = local_cursor.fetchall()
#                 cursor.execute("SELECT id, bill_name FROM asset_bills WHERE asset_id = %s", (mysql_id,))
#                 existing_bills = {row[1]: row[0] for row in cursor.fetchall()}
#                 for bill in bills:
#                     bill_id, asset_id, bill_name, bill_data, last_sync = bill
#                     if bill_name in existing_bills:
#                         cursor.execute("""
#                             UPDATE asset_bills SET bill_data = %s WHERE id = %s
#                         """, (bill_data, existing_bills[bill_name]))
#                     else:
#                         cursor.execute("""
#                             INSERT INTO asset_bills (asset_id, bill_name, bill_data)
#                             VALUES (%s, %s, %s)
#                         """, (mysql_id, bill_name, bill_data))

#             conn.commit()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text("Sync to server completed!"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#             self.refresh_local_assets()
#         except Error as e:
#             conn.rollback()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Sync error: {e}"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#         finally:
#             if 'cursor' in locals():
#                 cursor.close()
#             if 'conn' in locals():
#                 conn.close()
#             if 'local_cursor' in locals():
#                 local_cursor.close()
#             self.page.update()

#     def load_assets(self):
#         pass

#     def update_table(self):
#         pass

#     def open_edit_dialog(self, asset_id):
#         self.edit_dialog = AssetEditPage(self.page, self, asset_id=asset_id, local_db=self.local_db)
#         self.edit_dialog.open_dialog()



# import os
# os.environ["FLET_SECRET_KEY"] = "mysecret123"
# import flet as ft
# import mysql.connector
# from mysql.connector import Error
# import sqlite3
# from assetpage import AssetFormPage
# from assetedit import AssetEditPage
# import time

# class AssetPage(ft.Container):
#     def __init__(self, page: ft.Page):
#         super().__init__()

#         self.page = page
#         self.page.title = "Asset Management"
    
#         self.page.window.width = 365
#         self.page.window.height = 600
#         self.page.window.min_width = 360
#         self.page.window.min_height = 600
#         self.page.theme_mode = ft.ThemeMode.LIGHT
#         self.page.bgcolor = ft.Colors.WHITE

#         self.local_db = sqlite3.connect("assets.db", check_same_thread=False)
#         self.initialize_local_db()
        
#         self.add_asset_dialog = AssetFormPage(self.page, self, local_db=self.local_db)
        
#         self.page.appbar = ft.AppBar(
#             title=ft.Text("Asset Management", size=15, weight="bold"),
#             bgcolor=ft.Colors.GREEN_300,
#             color=ft.Colors.WHITE,
#             center_title=True,
#             automatically_imply_leading=False,
#         )

#         self.page.bottom_appbar = ft.BottomAppBar(
#             bgcolor=ft.Colors.BLUE,
#             shape=ft.NotchShape.CIRCULAR,
#             content=ft.Row(
#                 controls=[
#                     ft.PopupMenuButton(
#                         items=[
#                             ft.PopupMenuItem(text="Option 1"),
#                             ft.PopupMenuItem(text="Option 2"),
#                             ft.PopupMenuItem(text="Option 3"),
#                             ft.PopupMenuItem(text="Option 4"),
#                         ],
#                         icon=ft.Icon(ft.Icons.MENU_BOOK, color=ft.Colors.WHITE),
#                         tooltip="Menu Options",
#                     ),
#                     ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE, tooltip="Search"),
#                     ft.Container(expand=True),
#                     ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE, tooltip="Favorites"),
#                 ],
#             ),
#         )

#         self.expand = True
#         self.asset_add = []

#         self.add_asset_button = ft.ElevatedButton(
#             text="Add Asset",
#             icon=ft.Icons.ADD,
#             bgcolor=ft.Colors.TEAL_600,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#         )

#         self.Home_button = ft.ElevatedButton(
#             text="HOME",
#             icon=ft.Icons.HOME,
#             bgcolor=ft.Colors.GREEN_400,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.page.go("/"),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#         )

#         # Initialize local asset table with dynamic width
#         self.local_asset_table = ft.DataTable(
#             columns=[
#                 ft.DataColumn(ft.Text("ID")),
#                 ft.DataColumn(ft.Text("Model")),
#                 ft.DataColumn(ft.Text("Serial Number")),
#                 ft.DataColumn(ft.Text("Company")),
#                 ft.DataColumn(ft.Text("Location")),
#                 ft.DataColumn(ft.Text("Purchase Date")),
#                 ft.DataColumn(ft.Text("Status")),
#                 ft.DataColumn(ft.Text("Edit")),
#             ],
#             rows=[],
#         )

#         self.sync_from_server_button = ft.ElevatedButton(
#             text="Sync from Server",
#             icon=ft.Icons.DOWNLOAD,
#             bgcolor=ft.Colors.PURPLE_500,
#             color=ft.Colors.WHITE,
#             on_click=self.sync_from_server,
#             width=150,
#             height=40,
#         )

#         self.sync_to_server_button = ft.ElevatedButton(
#             text="Sync to Server",
#             icon=ft.Icons.UPLOAD,
#             bgcolor=ft.Colors.PINK_500,
#             color=ft.Colors.WHITE,
#             on_click=self.sync_to_server,
#             width=150,
#             height=40,
#         )

#         self.content = ft.Container(
#             content=ft.Column(
#                 controls=[
#                     ft.Row(
#                         controls=[self.Home_button, self.add_asset_button],
#                         alignment=ft.MainAxisAlignment.START,
#                         spacing=10,
#                     ),
#                     ft.Text("Local Assets", size=18, weight=ft.FontWeight.BOLD),
#                     ft.Container(
#                         content=self.local_asset_table,
#                         expand=True,
#                         width=self.page.window.width,  # Dynamic width based on window minus padding
#                         clip_behavior=ft.ClipBehavior.HARD_EDGE,
#                         padding=5,
#                         border_radius=10,
#                         bgcolor=ft.Colors.LIGHT_BLUE_100,
#                         border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#                     ),
#                     ft.Row(
#                         controls=[self.sync_from_server_button, self.sync_to_server_button],
#                         alignment=ft.MainAxisAlignment.CENTER,
#                         spacing=10,
#                     ),
#                 ],
#                 expand=True,
#                 spacing=10,
#                 scroll=ft.ScrollMode.AUTO,
#             ),
#             padding=10,
#         )

#         # Load initial local assets
#         self.refresh_local_assets()
#         self.page.add(self)
#         self.page.update()

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

#     def refresh_local_assets(self):
#         cursor = self.local_db.cursor()
#         try:
#             cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status, last_sync FROM assets")
#             assets = cursor.fetchall()
#             print(f"SQLite3 query returned {len(assets)} assets: {[row[2] for row in assets]}")

#             self.local_asset_table.rows.clear()

#             if not assets:
#                 self.local_asset_table.rows.append(
#                     ft.DataRow(
#                         cells=[
#                             ft.DataCell(ft.Text("No local assets found in SQLite3.")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                         ]
#                     )
#                 )
#             else:
#                 for asset in assets:
#                     asset_id, model, serial_number, company, location, purchase_date, status, last_sync = asset
#                     edit_button = ft.IconButton(
#                         icon=ft.Icons.EDIT,
#                         icon_color=ft.Colors.BLUE,
#                         bgcolor=ft.LinearGradient(
#                             begin=ft.alignment.top_left,
#                             end=ft.alignment.bottom_right,
#                             colors=[ft.Colors.BLUE_500, ft.Colors.BLUE_700]
#                         ),
#                         style=ft.ButtonStyle(
#                             shape=ft.RoundedRectangleBorder(radius=8),
#                             overlay_color=ft.Colors.BLUE_400
#                         ),
#                         tooltip="Edit Asset",
#                         on_click=lambda e, aid=asset_id: self.open_edit_dialog(aid)
#                     )
#                     self.local_asset_table.rows.append(
#                         ft.DataRow(
#                             cells=[
#                                 ft.DataCell(ft.Text(str(asset_id))),
#                                 ft.DataCell(ft.Text(model or "N/A")),
#                                 ft.DataCell(ft.Text(serial_number or "N/A")),
#                                 ft.DataCell(ft.Text(company or "N/A")),
#                                 ft.DataCell(ft.Text(location or "N/A")),
#                                 ft.DataCell(ft.Text(purchase_date or "N/A")),
#                                 ft.DataCell(ft.Text(status or "N/A")),
#                                 ft.DataCell(ft.Container(content=edit_button, alignment=ft.alignment.center)),
#                             ]
#                         )
#                     )

#             self.page.update()
#         except Exception as e:
#             print(f"Error fetching local asset data from SQLite3: {e}")
#             self.local_asset_table.rows.clear()
#             self.local_asset_table.rows.append(
#                 ft.DataRow(
#                     cells=[
#                         ft.DataCell(ft.Text(f"Error: {e}")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                     ]
#                 )
#             )
#             self.page.update()
#         finally:
#             cursor.close()

#     def sync_from_server(self, e):
#         db_config = {"host": "200.200.200.23", "user": "root", "password": "Pak@123", "database": "asm_sys"}
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             local_cursor = self.local_db.cursor()

#             local_cursor.execute("BEGIN TRANSACTION")
#             cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status FROM assets")
#             mysql_assets = cursor.fetchall()

#             for asset in mysql_assets:
#                 mysql_id, model, serial_number, company, location, purchase_date, status = asset
#                 local_cursor.execute("SELECT id FROM assets WHERE serial_number = ?", (serial_number,))
#                 existing_asset = local_cursor.fetchone()
#                 if existing_asset:
#                     local_id = existing_asset[0]
#                     local_cursor.execute("""
#                         UPDATE assets SET model = ?, company = ?, location = ?, purchase_date = ?, status = ?, last_sync = ?
#                         WHERE id = ?
#                     """, (model, company, location, purchase_date, status, time.strftime("%Y-%m-%d %H:%M:%S"), local_id))
#                 else:
#                     local_cursor.execute("""
#                         INSERT INTO assets (model, serial_number, company, location, purchase_date, status, last_sync)
#                         VALUES (?, ?, ?, ?, ?, ?, ?)
#                     """, (model, serial_number, company, location, purchase_date, status, time.strftime("%Y-%m-%d %H:%M:%S")))

#                 cursor.execute("SELECT id, asset_id, image_name, image_data FROM asset_images WHERE asset_id = %s", (mysql_id,))
#                 mysql_images = cursor.fetchall()
#                 local_cursor.execute("SELECT id, image_name FROM asset_images WHERE asset_id = (SELECT id FROM assets WHERE serial_number = ?)", (serial_number,))
#                 existing_images = {row[1]: row[0] for row in local_cursor.fetchall()}
#                 for img in mysql_images:
#                     img_id, asset_id, image_name, image_data = img
#                     if image_name in existing_images:
#                         local_cursor.execute("""
#                             UPDATE asset_images SET image_data = ?, last_sync = ? WHERE id = ?
#                         """, (image_data, time.strftime("%Y-%m-%d %H:%M:%S"), existing_images[image_name]))
#                     else:
#                         local_cursor.execute("""
#                             INSERT INTO asset_images (asset_id, image_name, image_data, last_sync)
#                             VALUES ((SELECT id FROM assets WHERE serial_number = ?), ?, ?, ?)
#                         """, (serial_number, image_name, image_data, time.strftime("%Y-%m-%d %H:%M:%S")))

#                 cursor.execute("SELECT id, asset_id, bill_name, bill_data FROM asset_bills WHERE asset_id = %s", (mysql_id,))
#                 mysql_bills = cursor.fetchall()
#                 local_cursor.execute("SELECT id, bill_name FROM asset_bills WHERE asset_id = (SELECT id FROM assets WHERE serial_number = ?)", (serial_number,))
#                 existing_bills = {row[1]: row[0] for row in cursor.fetchall()}
#                 for bill in mysql_bills:
#                     bill_id, asset_id, bill_name, bill_data = bill
#                     if bill_name in existing_bills:
#                         local_cursor.execute("""
#                             UPDATE asset_bills SET bill_data = ?, last_sync = ? WHERE id = ?
#                         """, (bill_data, time.strftime("%Y-%m-%d %H:%M:%S"), existing_bills[bill_name]))
#                     else:
#                         local_cursor.execute("""
#                             INSERT INTO asset_bills (asset_id, bill_name, bill_data, last_sync)
#                             VALUES ((SELECT id FROM assets WHERE serial_number = ?), ?, ?, ?)
#                         """, (serial_number, bill_name, bill_data, time.strftime("%Y-%m-%d %H:%M:%S")))

#             self.local_db.commit()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text("Sync from server completed!"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#             self.refresh_local_assets()
#         except Error as e:
#             self.local_db.rollback()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Sync error: {e}"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#         finally:
#             if 'cursor' in locals():
#                 cursor.close()
#             if 'conn' in locals():
#                 conn.close()
#             if 'local_cursor' in locals():
#                 local_cursor.close()
#             self.page.update()

#     def sync_to_server(self, e):
#         db_config = {"host": "200.200.200.23", "user": "root", "password": "Pak@123", "database": "asm_sys"}
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             local_cursor = self.local_db.cursor()

#             cursor.execute("BEGIN")
#             local_cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status, last_sync FROM assets")
#             local_assets = local_cursor.fetchall()

#             for asset in local_assets:
#                 local_id, model, serial_number, company, location, purchase_date, status, last_sync = asset
#                 cursor.execute("SELECT id FROM assets WHERE serial_number = %s", (serial_number,))
#                 existing_asset = cursor.fetchone()
#                 if existing_asset:
#                     mysql_id = existing_asset[0]
#                     cursor.execute("""
#                         UPDATE assets SET model = %s, company = %s, location = %s, purchase_date = %s, status = %s
#                         WHERE id = %s
#                     """, (model, company, location, purchase_date, status, mysql_id))
#                 else:
#                     cursor.execute("""
#                         INSERT INTO assets (model, serial_number, company, location, purchase_date, status)
#                         VALUES (%s, %s, %s, %s, %s, %s)
#                     """, (model, serial_number, company, location, purchase_date, status))
#                     mysql_id = cursor.lastrowid

#                 local_cursor.execute("SELECT id, asset_id, image_name, image_data, last_sync FROM asset_images WHERE asset_id = ?", (local_id,))
#                 images = local_cursor.fetchall()
#                 cursor.execute("SELECT id, image_name FROM asset_images WHERE asset_id = %s", (mysql_id,))
#                 existing_images = {row[0]: row[1] for row in cursor.fetchall()}
#                 for img in images:
#                     img_id, asset_id, image_name, image_data, last_sync = img
#                     if img_id in existing_images:
#                         cursor.execute("""
#                             UPDATE asset_images SET image_name = %s, image_data = %s WHERE id = %s AND asset_id = %s
#                         """, (image_name, image_data, img_id, mysql_id))
#                     else:
#                         cursor.execute("""
#                             INSERT INTO asset_images (asset_id, image_name, image_data)
#                             VALUES (%s, %s, %s)
#                         """, (mysql_id, image_name, image_data))

#                 local_cursor.execute("SELECT id, asset_id, bill_name, bill_data, last_sync FROM asset_bills WHERE asset_id = ?", (local_id,))
#                 bills = local_cursor.fetchall()
#                 cursor.execute("SELECT id, bill_name FROM asset_bills WHERE asset_id = %s", (mysql_id,))
#                 existing_bills = {row[1]: row[0] for row in cursor.fetchall()}
#                 for bill in bills:
#                     bill_id, asset_id, bill_name, bill_data, last_sync = bill
#                     if bill_name in existing_bills:
#                         cursor.execute("""
#                             UPDATE asset_bills SET bill_data = %s WHERE id = %s
#                         """, (bill_data, existing_bills[bill_name]))
#                     else:
#                         cursor.execute("""
#                             INSERT INTO asset_bills (asset_id, bill_name, bill_data)
#                             VALUES (%s, %s, %s)
#                         """, (mysql_id, bill_name, bill_data))

#             conn.commit()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text("Sync to server completed!"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#             self.refresh_local_assets()
#         except Error as e:
#             conn.rollback()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Sync error: {e}"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#         finally:
#             if 'cursor' in locals():
#                 cursor.close()
#             if 'conn' in locals():
#                 conn.close()
#             if 'local_cursor' in locals():
#                 local_cursor.close()
#             self.page.update()

#     def load_assets(self):
#         pass

#     def update_table(self):
#         pass

#     def open_edit_dialog(self, asset_id):
#         self.edit_dialog = AssetEditPage(self.page, self, asset_id=asset_id, local_db=self.local_db)
#         self.edit_dialog.open_dialog()



# import os
# os.environ["FLET_SECRET_KEY"] = "mysecret123"
# import flet as ft
# import mysql.connector
# from mysql.connector import Error
# import sqlite3
# from assetpage import AssetFormPage
# from assetedit import AssetEditPage

# class AssetPage(ft.Container):
#     def __init__(self, page: ft.Page):
#         super().__init__()

#         self.page = page
#         self.page.title = "Asset Management"
    
#         self.page.window.width = 365
#         self.page.window.height = 600
#         self.page.window.min_width = 360
#         self.page.window.min_height = 600
#         self.page.theme_mode = ft.ThemeMode.LIGHT
#         self.page.bgcolor = ft.Colors.WHITE

#         self.local_db = sqlite3.connect("assets.db", check_same_thread=False)
#         self.initialize_local_db()
        
#         self.add_asset_dialog = AssetFormPage(self.page, self, local_db=self.local_db)
        
#         self.page.appbar = ft.AppBar(
#             title=ft.Text("Asset Management", size=15, weight="bold"),
#             bgcolor=ft.Colors.GREEN_300,
#             color=ft.Colors.WHITE,
#             center_title=True,
#             automatically_imply_leading=False,
#         )

#         self.page.bottom_appbar = ft.BottomAppBar(
#             bgcolor=ft.Colors.BLUE,
#             shape=ft.NotchShape.CIRCULAR,
#             content=ft.Row(
#                 controls=[
#                     ft.PopupMenuButton(
#                         items=[
#                             ft.PopupMenuItem(text="Option 1"),
#                             ft.PopupMenuItem(text="Option 2"),
#                             ft.PopupMenuItem(text="Option 3"),
#                             ft.PopupMenuItem(text="Option 4"),
#                         ],
#                         icon=ft.Icon(ft.Icons.MENU_BOOK, color=ft.Colors.WHITE),
#                         tooltip="Menu Options",
#                     ),
#                     ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE, tooltip="Search"),
#                     ft.Container(expand=True),
#                     ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE, tooltip="Favorites"),
#                 ],
#             ),
#         )

#         self.expand = True
#         self.asset_add = []

#         self.add_asset_button = ft.ElevatedButton(
#             text="Add Asset",
#             icon=ft.Icons.ADD,
#             bgcolor=ft.Colors.TEAL_600,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#         )

#         self.Home_button = ft.ElevatedButton(
#             text="HOME",
#             icon=ft.Icons.HOME,
#             bgcolor=ft.Colors.GREEN_400,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.page.go("/"),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#         )

#         # Initialize local asset table with styled columns
#         self.local_asset_table = ft.DataTable(
#             columns=[
#                 ft.DataColumn(ft.Text("ID", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Model", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Serial Number", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Company", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Location", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Purchase Date", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Status", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Edit", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#             ],
#             rows=[],
#             border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#             vertical_lines=ft.border.BorderSide(1, ft.Colors.BLUE_GREY_300),
#             column_spacing=5,
#         )

#         self.sync_from_server_button = ft.ElevatedButton(
#             text="Sync from Server",
#             icon=ft.Icons.DOWNLOAD,
#             bgcolor=ft.Colors.PURPLE_500,
#             color=ft.Colors.WHITE,
#             on_click=self.sync_from_server,
#             width=150,
#             height=40,
#         )

#         self.sync_to_server_button = ft.ElevatedButton(
#             text="Sync to Server",
#             icon=ft.Icons.UPLOAD,
#             bgcolor=ft.Colors.PINK_500,
#             color=ft.Colors.WHITE,
#             on_click=self.sync_to_server,
#             width=150,
#             height=40,
#         )

#         self.content = ft.Container(
#             content=ft.Column(
#                 controls=[
#                     ft.Row(
#                         controls=[self.Home_button, self.add_asset_button],
#                         alignment=ft.MainAxisAlignment.START,
#                         spacing=10,
#                     ),
#                     ft.Text("Local Assets", size=18, weight=ft.FontWeight.BOLD),
#                     ft.Container(
#                         content=self.local_asset_table,
#                         expand=True,
#                         width=self.page.window.width - 20,
#                         clip_behavior=ft.ClipBehavior.HARD_EDGE,
#                         padding=5,
#                         border_radius=10,
#                         bgcolor=ft.Colors.LIGHT_BLUE_100,
#                         border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#                     ),
#                     ft.Row(
#                         controls=[self.sync_from_server_button, self.sync_to_server_button],
#                         alignment=ft.MainAxisAlignment.CENTER,
#                         spacing=10,
#                     ),
#                 ],
#                 expand=True,
#                 spacing=10,
#                 scroll=ft.ScrollMode.AUTO,
#             ),
#             padding=10,
#         )

#         # Load initial local assets
#         self.refresh_local_assets()
#         self.page.add(self)
#         self.page.update()

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

#     def refresh_local_assets(self):
#         cursor = self.local_db.cursor()
#         try:
#             cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status, last_sync FROM assets")
#             assets = cursor.fetchall()
#             print(f"SQLite3 query returned {len(assets)} assets: {[row[2] for row in assets]}")

#             self.local_asset_table.rows.clear()

#             if not assets:
#                 self.local_asset_table.rows.append(
#                     ft.DataRow(
#                         cells=[
#                             ft.DataCell(ft.Text("No local assets found in SQLite3.")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                         ]
#                     )
#                 )
#             else:
#                 for i, asset in enumerate(assets):
#                     asset_id, model, serial_number, company, location, purchase_date, status, last_sync = asset
#                     edit_button = ft.IconButton(
#                         icon=ft.Icons.EDIT,
#                         icon_color=ft.Colors.BLUE,
#                         bgcolor=ft.LinearGradient(
#                             begin=ft.alignment.top_left,
#                             end=ft.alignment.bottom_right,
#                             colors=[ft.Colors.BLUE_500, ft.Colors.BLUE_700]
#                         ),
#                         style=ft.ButtonStyle(
#                             shape=ft.RoundedRectangleBorder(radius=8),
#                             overlay_color=ft.Colors.BLUE_400
#                         ),
#                         tooltip="Edit Asset",
#                         on_click=lambda e, aid=asset_id: self.open_edit_dialog(aid)
#                     )
#                     self.local_asset_table.rows.append(
#                         ft.DataRow(
#                             cells=[
#                                 ft.DataCell(ft.Text(str(asset_id), color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Text(model or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Text(serial_number or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Text(company or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Text(location or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Text(purchase_date or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Text(status or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Container(content=edit_button, alignment=ft.alignment.center)),
#                             ],
#                             color=ft.Colors.WHITE if i % 2 == 0 else ft.Colors.BLUE_GREY_50
#                         )
#                     )

#             self.page.update()
#         except Exception as e:
#             print(f"Error fetching local asset data from SQLite3: {e}")
#             self.local_asset_table.rows.clear()
#             self.local_asset_table.rows.append(
#                 ft.DataRow(
#                     cells=[
#                         ft.DataCell(ft.Text(f"Error: {e}")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                     ]
#                 )
#             )
#             self.page.update()
#         finally:
#             cursor.close()

#     def sync_from_server(self, e):
#         db_config = {"host": "200.200.200.23", "user": "root", "password": "Pak@123", "database": "asm_sys"}
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             local_cursor = self.local_db.cursor()

#             local_cursor.execute("BEGIN TRANSACTION")
#             cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status FROM assets")
#             mysql_assets = cursor.fetchall()

#             for asset in mysql_assets:
#                 mysql_id, model, serial_number, company, location, purchase_date, status = asset
#                 local_cursor.execute("SELECT id FROM assets WHERE serial_number = ?", (serial_number,))
#                 existing_asset = local_cursor.fetchone()
#                 if existing_asset:
#                     local_id = existing_asset[0]
#                     local_cursor.execute("""
#                         UPDATE assets SET model = ?, company = ?, location = ?, purchase_date = ?, status = ?, last_sync = ?
#                         WHERE id = ?
#                     """, (model, company, location, purchase_date, status, time.strftime("%Y-%m-%d %H:%M:%S"), local_id))
#                 else:
#                     local_cursor.execute("""
#                         INSERT INTO assets (model, serial_number, company, location, purchase_date, status, last_sync)
#                         VALUES (?, ?, ?, ?, ?, ?, ?)
#                     """, (model, serial_number, company, location, purchase_date, status, time.strftime("%Y-%m-%d %H:%M:%S")))

#                 cursor.execute("SELECT id, asset_id, image_name, image_data FROM asset_images WHERE asset_id = %s", (mysql_id,))
#                 mysql_images = cursor.fetchall()
#                 local_cursor.execute("SELECT id, image_name FROM asset_images WHERE asset_id = (SELECT id FROM assets WHERE serial_number = ?)", (serial_number,))
#                 existing_images = {row[1]: row[0] for row in local_cursor.fetchall()}
#                 for img in mysql_images:
#                     img_id, asset_id, image_name, image_data = img
#                     if image_name in existing_images:
#                         local_cursor.execute("""
#                             UPDATE asset_images SET image_data = ?, last_sync = ? WHERE id = ?
#                         """, (image_data, time.strftime("%Y-%m-%d %H:%M:%S"), existing_images[image_name]))
#                     else:
#                         local_cursor.execute("""
#                             INSERT INTO asset_images (asset_id, image_name, image_data, last_sync)
#                             VALUES ((SELECT id FROM assets WHERE serial_number = ?), ?, ?, ?)
#                         """, (serial_number, image_name, image_data, time.strftime("%Y-%m-%d %H:%M:%S")))

#                 cursor.execute("SELECT id, asset_id, bill_name, bill_data FROM asset_bills WHERE asset_id = %s", (mysql_id,))
#                 mysql_bills = cursor.fetchall()
#                 local_cursor.execute("SELECT id, bill_name FROM asset_bills WHERE asset_id = (SELECT id FROM assets WHERE serial_number = ?)", (serial_number,))
#                 existing_bills = {row[1]: row[0] for row in cursor.fetchall()}
#                 for bill in mysql_bills:
#                     bill_id, asset_id, bill_name, bill_data = bill
#                     if bill_name in existing_bills:
#                         local_cursor.execute("""
#                             UPDATE asset_bills SET bill_data = ?, last_sync = ? WHERE id = ?
#                         """, (bill_data, time.strftime("%Y-%m-%d %H:%M:%S"), existing_bills[bill_name]))
#                     else:
#                         local_cursor.execute("""
#                             INSERT INTO asset_bills (asset_id, bill_name, bill_data, last_sync)
#                             VALUES ((SELECT id FROM assets WHERE serial_number = ?), ?, ?, ?)
#                         """, (serial_number, bill_name, bill_data, time.strftime("%Y-%m-%d %H:%M:%S")))

#             self.local_db.commit()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text("Sync from server completed!"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#             self.refresh_local_assets()
#         except Error as e:
#             self.local_db.rollback()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Sync error: {e}"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#         finally:
#             if 'cursor' in locals():
#                 cursor.close()
#             if 'conn' in locals():
#                 conn.close()
#             if 'local_cursor' in locals():
#                 local_cursor.close()
#             self.page.update()

#     def sync_to_server(self, e):
#         db_config = {"host": "200.200.200.23", "user": "root", "password": "Pak@123", "database": "asm_sys"}
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             local_cursor = self.local_db.cursor()

#             cursor.execute("BEGIN")
#             local_cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status, last_sync FROM assets")
#             local_assets = local_cursor.fetchall()

#             for asset in local_assets:
#                 local_id, model, serial_number, company, location, purchase_date, status, last_sync = asset
#                 cursor.execute("SELECT id FROM assets WHERE serial_number = %s", (serial_number,))
#                 existing_asset = cursor.fetchone()
#                 if existing_asset:
#                     mysql_id = existing_asset[0]
#                     cursor.execute("""
#                         UPDATE assets SET model = %s, company = %s, location = %s, purchase_date = %s, status = %s
#                         WHERE id = %s
#                     """, (model, company, location, purchase_date, status, mysql_id))
#                 else:
#                     cursor.execute("""
#                         INSERT INTO assets (model, serial_number, company, location, purchase_date, status)
#                         VALUES (%s, %s, %s, %s, %s, %s)
#                     """, (model, serial_number, company, location, purchase_date, status))
#                     mysql_id = cursor.lastrowid

#                 local_cursor.execute("SELECT id, asset_id, image_name, image_data, last_sync FROM asset_images WHERE asset_id = ?", (local_id,))
#                 images = local_cursor.fetchall()
#                 cursor.execute("SELECT id, image_name FROM asset_images WHERE asset_id = %s", (mysql_id,))
#                 existing_images = {row[0]: row[1] for row in cursor.fetchall()}
#                 for img in images:
#                     img_id, asset_id, image_name, image_data, last_sync = img
#                     if img_id in existing_images:
#                         cursor.execute("""
#                             UPDATE asset_images SET image_name = %s, image_data = %s WHERE id = %s AND asset_id = %s
#                         """, (image_name, image_data, img_id, mysql_id))
#                     else:
#                         cursor.execute("""
#                             INSERT INTO asset_images (asset_id, image_name, image_data)
#                             VALUES (%s, %s, %s)
#                         """, (mysql_id, image_name, image_data))

#                 local_cursor.execute("SELECT id, asset_id, bill_name, bill_data, last_sync FROM asset_bills WHERE asset_id = ?", (local_id,))
#                 bills = local_cursor.fetchall()
#                 cursor.execute("SELECT id, bill_name FROM asset_bills WHERE asset_id = %s", (mysql_id,))
#                 existing_bills = {row[1]: row[0] for row in cursor.fetchall()}
#                 for bill in bills:
#                     bill_id, asset_id, bill_name, bill_data, last_sync = bill
#                     if bill_name in existing_bills:
#                         cursor.execute("""
#                             UPDATE asset_bills SET bill_data = %s WHERE id = %s
#                         """, (bill_data, existing_bills[bill_name]))
#                     else:
#                         cursor.execute("""
#                             INSERT INTO asset_bills (asset_id, bill_name, bill_data)
#                             VALUES (%s, %s, %s)
#                         """, (mysql_id, bill_name, bill_data))

#             conn.commit()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text("Sync to server completed!"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#             self.refresh_local_assets()
#         except Error as e:
#             conn.rollback()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Sync error: {e}"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#         finally:
#             if 'cursor' in locals():
#                 cursor.close()
#             if 'conn' in locals():
#                 conn.close()
#             if 'local_cursor' in locals():
#                 local_cursor.close()
#             self.page.update()

#     def load_assets(self):
#         pass

#     def update_table(self):
#         pass

#     def open_edit_dialog(self, asset_id):
#         self.edit_dialog = AssetEditPage(self.page, self, asset_id=asset_id, local_db=self.local_db)
#         self.edit_dialog.open_dialog()



# import os
# os.environ["FLET_SECRET_KEY"] = "mysecret123"
# import flet as ft
# import mysql.connector
# from mysql.connector import Error
# import sqlite3
# from assetpage import AssetFormPage
# from assetedit import AssetEditPage

# class AssetPage(ft.Container):
#     def __init__(self, page: ft.Page):
#         super().__init__()

#         self.page = page
#         self.page.title = "Asset Management"
    
#         self.page.window.width = 365
#         self.page.window.height = 600
#         self.page.window.min_width = 360
#         self.page.window.min_height = 600
#         self.page.theme_mode = ft.ThemeMode.LIGHT
#         self.page.bgcolor = ft.Colors.WHITE

#         self.local_db = sqlite3.connect("assets.db", check_same_thread=False)
#         self.initialize_local_db()
        
#         self.add_asset_dialog = AssetFormPage(self.page, self, local_db=self.local_db)
        
#         self.page.appbar = ft.AppBar(
#             title=ft.Text("Asset Management", size=15, weight="bold"),
#             bgcolor=ft.Colors.GREEN_300,
#             color=ft.Colors.WHITE,
#             center_title=True,
#             automatically_imply_leading=False,
#         )

#         self.page.bottom_appbar = ft.BottomAppBar(
#             bgcolor=ft.Colors.BLUE,
#             shape=ft.NotchShape.CIRCULAR,
#             content=ft.Row(
#                 controls=[
#                     ft.PopupMenuButton(
#                         items=[
#                             ft.PopupMenuItem(text="Option 1"),
#                             ft.PopupMenuItem(text="Option 2"),
#                             ft.PopupMenuItem(text="Option 3"),
#                             ft.PopupMenuItem(text="Option 4"),
#                         ],
#                         icon=ft.Icon(ft.Icons.MENU_BOOK, color=ft.Colors.WHITE),
#                         tooltip="Menu Options",
#                     ),
#                     ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE, tooltip="Search"),
#                     ft.Container(expand=True),
#                     ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE, tooltip="Favorites"),
#                 ],
#             ),
#         )

#         self.expand = True
#         self.asset_add = []

#         self.add_asset_button = ft.ElevatedButton(
#             text="Add Asset",
#             icon=ft.Icons.ADD,
#             bgcolor=ft.Colors.TEAL_600,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#         )

#         self.Home_button = ft.ElevatedButton(
#             text="HOME",
#             icon=ft.Icons.HOME,
#             bgcolor=ft.Colors.GREEN_400,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.page.go("/"),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#         )

#         # Initialize local asset table with selected columns
#         self.local_asset_table = ft.DataTable(
#             columns=[
#                 ft.DataColumn(ft.Text("Model", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Serial Number", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Location", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Edit", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#             ],
#             rows=[],
#             border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#             vertical_lines=ft.border.BorderSide(1, ft.Colors.BLUE_GREY_300),
#             column_spacing=5,
#         )

#         self.sync_from_server_button = ft.ElevatedButton(
#             text="Sync from Server",
#             icon=ft.Icons.DOWNLOAD,
#             bgcolor=ft.Colors.PURPLE_500,
#             color=ft.Colors.WHITE,
#             on_click=self.sync_from_server,
#             width=150,
#             height=40,
#         )

#         self.sync_to_server_button = ft.ElevatedButton(
#             text="Sync to Server",
#             icon=ft.Icons.UPLOAD,
#             bgcolor=ft.Colors.PINK_500,
#             color=ft.Colors.WHITE,
#             on_click=self.sync_to_server,
#             width=150,
#             height=40,
#         )

#         self.content = ft.Container(
#             content=ft.Column(
#                 controls=[
#                     ft.Row(
#                         controls=[self.Home_button, self.add_asset_button],
#                         alignment=ft.MainAxisAlignment.START,
#                         spacing=10,
#                     ),
#                     ft.Text("Local Assets", size=18, weight=ft.FontWeight.BOLD),
#                     ft.Container(
#                         content=self.local_asset_table,
#                         expand=True,
#                         width=self.page.window.width - 20,
#                         clip_behavior=ft.ClipBehavior.HARD_EDGE,
#                         padding=5,
#                         border_radius=10,
#                         bgcolor=ft.Colors.LIGHT_BLUE_100,
#                         border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#                     ),
#                     ft.Row(
#                         controls=[self.sync_from_server_button, self.sync_to_server_button],
#                         alignment=ft.MainAxisAlignment.CENTER,
#                         spacing=10,
#                     ),
#                 ],
#                 expand=True,
#                 spacing=10,
#                 scroll=ft.ScrollMode.AUTO,
#             ),
#             padding=10,
#         )

#         # Load initial local assets
#         self.refresh_local_assets()
#         self.page.add(self)
#         self.page.update()

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

#     def refresh_local_assets(self):
#         cursor = self.local_db.cursor()
#         try:
#             cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status, last_sync FROM assets")
#             assets = cursor.fetchall()
#             print(f"SQLite3 query returned {len(assets)} assets: {[row[2] for row in assets]}")

#             self.local_asset_table.rows.clear()

#             if not assets:
#                 self.local_asset_table.rows.append(
#                     ft.DataRow(
#                         cells=[
#                             ft.DataCell(ft.Text("No local assets found in SQLite3.")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                         ]
#                     )
#                 )
#             else:
#                 for i, asset in enumerate(assets):
#                     asset_id, model, serial_number, company, location, purchase_date, status, last_sync = asset
#                     edit_button = ft.IconButton(
#                         icon=ft.Icons.EDIT,
#                         icon_color=ft.Colors.BLUE,
#                         bgcolor=ft.LinearGradient(
#                             begin=ft.alignment.top_left,
#                             end=ft.alignment.bottom_right,
#                             colors=[ft.Colors.BLUE_500, ft.Colors.BLUE_700]
#                         ),
#                         style=ft.ButtonStyle(
#                             shape=ft.RoundedRectangleBorder(radius=8),
#                             overlay_color=ft.Colors.BLUE_400
#                         ),
#                         tooltip="Edit Asset",
#                         on_click=lambda e, aid=asset_id: self.open_edit_dialog(aid)
#                     )
#                     self.local_asset_table.rows.append(
#                         ft.DataRow(
#                             cells=[
#                                 ft.DataCell(ft.Text(model or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Text(serial_number or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Text(location or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Container(content=edit_button, alignment=ft.alignment.center)),
#                             ],
#                             color=ft.Colors.WHITE if i % 2 == 0 else ft.Colors.BLUE_GREY_50
#                         )
#                     )

#             self.page.update()
#         except Exception as e:
#             print(f"Error fetching local asset data from SQLite3: {e}")
#             self.local_asset_table.rows.clear()
#             self.local_asset_table.rows.append(
#                 ft.DataRow(
#                     cells=[
#                         ft.DataCell(ft.Text(f"Error: {e}")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                     ]
#                 )
#             )
#             self.page.update()
#         finally:
#             cursor.close()

#     def sync_from_server(self, e):
#         db_config = {"host": "200.200.200.23", "user": "root", "password": "Pak@123", "database": "asm_sys"}
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             local_cursor = self.local_db.cursor()

#             local_cursor.execute("BEGIN TRANSACTION")
#             cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status FROM assets")
#             mysql_assets = cursor.fetchall()

#             for asset in mysql_assets:
#                 mysql_id, model, serial_number, company, location, purchase_date, status = asset
#                 local_cursor.execute("SELECT id FROM assets WHERE serial_number = ?", (serial_number,))
#                 existing_asset = local_cursor.fetchone()
#                 if existing_asset:
#                     local_id = existing_asset[0]
#                     local_cursor.execute("""
#                         UPDATE assets SET model = ?, company = ?, location = ?, purchase_date = ?, status = ?, last_sync = ?
#                         WHERE id = ?
#                     """, (model, company, location, purchase_date, status, time.strftime("%Y-%m-%d %H:%M:%S"), local_id))
#                 else:
#                     local_cursor.execute("""
#                         INSERT INTO assets (model, serial_number, company, location, purchase_date, status, last_sync)
#                         VALUES (?, ?, ?, ?, ?, ?, ?)
#                     """, (model, serial_number, company, location, purchase_date, status, time.strftime("%Y-%m-%d %H:%M:%S")))

#                 cursor.execute("SELECT id, asset_id, image_name, image_data FROM asset_images WHERE asset_id = %s", (mysql_id,))
#                 mysql_images = cursor.fetchall()
#                 local_cursor.execute("SELECT id, image_name FROM asset_images WHERE asset_id = (SELECT id FROM assets WHERE serial_number = ?)", (serial_number,))
#                 existing_images = {row[1]: row[0] for row in local_cursor.fetchall()}
#                 for img in mysql_images:
#                     img_id, asset_id, image_name, image_data = img
#                     if image_name in existing_images:
#                         local_cursor.execute("""
#                             UPDATE asset_images SET image_data = ?, last_sync = ? WHERE id = ?
#                         """, (image_data, time.strftime("%Y-%m-%d %H:%M:%S"), existing_images[image_name]))
#                     else:
#                         local_cursor.execute("""
#                             INSERT INTO asset_images (asset_id, image_name, image_data, last_sync)
#                             VALUES ((SELECT id FROM assets WHERE serial_number = ?), ?, ?, ?)
#                         """, (serial_number, image_name, image_data, time.strftime("%Y-%m-%d %H:%M:%S")))

#                 cursor.execute("SELECT id, asset_id, bill_name, bill_data FROM asset_bills WHERE asset_id = %s", (mysql_id,))
#                 mysql_bills = cursor.fetchall()
#                 local_cursor.execute("SELECT id, bill_name FROM asset_bills WHERE asset_id = (SELECT id FROM assets WHERE serial_number = ?)", (serial_number,))
#                 existing_bills = {row[1]: row[0] for row in cursor.fetchall()}
#                 for bill in mysql_bills:
#                     bill_id, asset_id, bill_name, bill_data = bill
#                     if bill_name in existing_bills:
#                         local_cursor.execute("""
#                             UPDATE asset_bills SET bill_data = ?, last_sync = ? WHERE id = ?
#                         """, (bill_data, time.strftime("%Y-%m-%d %H:%M:%S"), existing_bills[bill_name]))
#                     else:
#                         local_cursor.execute("""
#                             INSERT INTO asset_bills (asset_id, bill_name, bill_data, last_sync)
#                             VALUES ((SELECT id FROM assets WHERE serial_number = ?), ?, ?, ?)
#                         """, (serial_number, bill_name, bill_data, time.strftime("%Y-%m-%d %H:%M:%S")))

#             self.local_db.commit()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text("Sync from server completed!"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#             self.refresh_local_assets()
#         except Error as e:
#             self.local_db.rollback()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Sync error: {e}"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#         finally:
#             if 'cursor' in locals():
#                 cursor.close()
#             if 'conn' in locals():
#                 conn.close()
#             if 'local_cursor' in locals():
#                 local_cursor.close()
#             self.page.update()

#     def sync_to_server(self, e):
#         db_config = {"host": "200.200.200.23", "user": "root", "password": "Pak@123", "database": "asm_sys"}
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             local_cursor = self.local_db.cursor()

#             cursor.execute("BEGIN")
#             local_cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status, last_sync FROM assets")
#             local_assets = local_cursor.fetchall()

#             for asset in local_assets:
#                 local_id, model, serial_number, company, location, purchase_date, status, last_sync = asset
#                 cursor.execute("SELECT id FROM assets WHERE serial_number = %s", (serial_number,))
#                 existing_asset = cursor.fetchone()
#                 if existing_asset:
#                     mysql_id = existing_asset[0]
#                     cursor.execute("""
#                         UPDATE assets SET model = %s, company = %s, location = %s, purchase_date = %s, status = %s
#                         WHERE id = %s
#                     """, (model, company, location, purchase_date, status, mysql_id))
#                 else:
#                     cursor.execute("""
#                         INSERT INTO assets (model, serial_number, company, location, purchase_date, status)
#                         VALUES (%s, %s, %s, %s, %s, %s)
#                     """, (model, serial_number, company, location, purchase_date, status))
#                     mysql_id = cursor.lastrowid

#                 local_cursor.execute("SELECT id, asset_id, image_name, image_data, last_sync FROM asset_images WHERE asset_id = ?", (local_id,))
#                 images = local_cursor.fetchall()
#                 cursor.execute("SELECT id, image_name FROM asset_images WHERE asset_id = %s", (mysql_id,))
#                 existing_images = {row[0]: row[1] for row in cursor.fetchall()}
#                 for img in images:
#                     img_id, asset_id, image_name, image_data, last_sync = img
#                     if img_id in existing_images:
#                         cursor.execute("""
#                             UPDATE asset_images SET image_name = %s, image_data = %s WHERE id = %s AND asset_id = %s
#                         """, (image_name, image_data, img_id, mysql_id))
#                     else:
#                         cursor.execute("""
#                             INSERT INTO asset_images (asset_id, image_name, image_data)
#                             VALUES (%s, %s, %s)
#                         """, (mysql_id, image_name, image_data))

#                 local_cursor.execute("SELECT id, asset_id, bill_name, bill_data, last_sync FROM asset_bills WHERE asset_id = ?", (local_id,))
#                 bills = local_cursor.fetchall()
#                 cursor.execute("SELECT id, bill_name FROM asset_bills WHERE asset_id = %s", (mysql_id,))
#                 existing_bills = {row[1]: row[0] for row in cursor.fetchall()}
#                 for bill in bills:
#                     bill_id, asset_id, bill_name, bill_data, last_sync = bill
#                     if bill_name in existing_bills:
#                         cursor.execute("""
#                             UPDATE asset_bills SET bill_data = %s WHERE id = %s
#                         """, (bill_data, existing_bills[bill_name]))
#                     else:
#                         cursor.execute("""
#                             INSERT INTO asset_bills (asset_id, bill_name, bill_data)
#                             VALUES (%s, %s, %s)
#                         """, (mysql_id, bill_name, bill_data))

#             conn.commit()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text("Sync to server completed!"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#             self.refresh_local_assets()
#         except Error as e:
#             conn.rollback()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Sync error: {e}"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#         finally:
#             if 'cursor' in locals():
#                 cursor.close()
#             if 'conn' in locals():
#                 conn.close()
#             if 'local_cursor' in locals():
#                 local_cursor.close()
#             self.page.update()

#     def load_assets(self):
#         pass

#     def update_table(self):
#         pass

#     def open_edit_dialog(self, asset_id):
#         self.edit_dialog = AssetEditPage(self.page, self, asset_id=asset_id, local_db=self.local_db)
#         self.edit_dialog.open_dialog()


# import os
# os.environ["FLET_SECRET_KEY"] = "mysecret123"
# import flet as ft
# import mysql.connector
# from mysql.connector import Error
# import sqlite3
# from assetpage import AssetFormPage
# from assetedit import AssetEditPage
# import time

# class AssetPage(ft.Container):
#     def __init__(self, page: ft.Page):
#         super().__init__()

#         self.page = page
#         self.page.title = "Asset Management"
    
#         self.page.window.width = 365
#         self.page.window.height = 600
#         self.page.window.min_width = 360
#         self.page.window.min_height = 600
#         self.page.theme_mode = ft.ThemeMode.LIGHT
#         self.page.bgcolor = ft.Colors.WHITE

#         self.local_db = sqlite3.connect("assets.db", check_same_thread=False)
#         self.initialize_local_db()
        
#         self.add_asset_dialog = AssetFormPage(self.page, self, local_db=self.local_db)
        
#         self.page.appbar = ft.AppBar(
#             title=ft.Text("Asset Management", size=15, weight="bold"),
#             bgcolor=ft.Colors.GREEN_300,
#             color=ft.Colors.WHITE,
#             center_title=True,
#             automatically_imply_leading=False,
#         )

#         self.page.bottom_appbar = ft.BottomAppBar(
#             bgcolor=ft.Colors.BLUE,
#             shape=ft.NotchShape.CIRCULAR,
#             content=ft.Row(
#                 controls=[
#                     ft.PopupMenuButton(
#                         items=[
#                             ft.PopupMenuItem(text="Option 1"),
#                             ft.PopupMenuItem(text="Option 2"),
#                             ft.PopupMenuItem(text="Option 3"),
#                             ft.PopupMenuItem(text="Option 4"),
#                         ],
#                         icon=ft.Icon(ft.Icons.MENU_BOOK, color=ft.Colors.WHITE),
#                         tooltip="Menu Options",
#                     ),
#                     ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE, tooltip="Search"),
#                     ft.Container(expand=True),
#                     ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE, tooltip="Favorites"),
#                 ],
#             ),
#         )

#         self.expand = True
#         self.asset_add = []

#         self.add_asset_button = ft.ElevatedButton(
#             text="Add Asset",
#             icon=ft.Icons.ADD,
#             bgcolor=ft.Colors.TEAL_600,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#         )

#         self.Home_button = ft.ElevatedButton(
#             text="HOME",
#             icon=ft.Icons.HOME,
#             bgcolor=ft.Colors.GREEN_400,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.page.go("/"),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#         )

#         # Initialize local asset table with selected columns
#         self.local_asset_table = ft.DataTable(
#             columns=[
#                 ft.DataColumn(ft.Text("Model", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Serial Number", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Location", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Edit", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#             ],
#             rows=[],
#             border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#             vertical_lines=ft.border.BorderSide(1, ft.Colors.BLUE_GREY_300),
#             column_spacing=5,
#         )

#         self.sync_from_server_button = ft.ElevatedButton(
#             text="Sync from Server",
#             icon=ft.Icons.DOWNLOAD,
#             bgcolor=ft.Colors.PURPLE_500,
#             color=ft.Colors.WHITE,
#             on_click=self.sync_from_server,
#             width=150,
#             height=40,
#         )

#         self.sync_to_server_button = ft.ElevatedButton(
#             text="Sync to Server",
#             icon=ft.Icons.UPLOAD,
#             bgcolor=ft.Colors.PINK_500,
#             color=ft.Colors.WHITE,
#             on_click=self.sync_to_server,
#             width=150,
#             height=40,
#         )

#         self.content = ft.Container(
#             content=ft.Column(
#                 controls=[
#                     ft.Row(
#                         controls=[self.Home_button, self.add_asset_button],
#                         alignment=ft.MainAxisAlignment.START,
#                         spacing=10,
#                     ),
#                     ft.Text("Local Assets", size=18, weight=ft.FontWeight.BOLD),
#                     ft.Container(
#                         content=self.local_asset_table,
#                         expand=True,
#                         width=self.page.window.width - 20,
#                         clip_behavior=ft.ClipBehavior.HARD_EDGE,
#                         padding=5,
#                         border_radius=10,
#                         bgcolor=ft.Colors.LIGHT_BLUE_100,
#                         border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#                     ),
#                     ft.Row(
#                         controls=[self.sync_from_server_button, self.sync_to_server_button],
#                         alignment=ft.MainAxisAlignment.CENTER,
#                         spacing=10,
#                     ),
#                 ],
#                 expand=True,
#                 spacing=10,
#                 scroll=ft.ScrollMode.AUTO,
#             ),
#             padding=10,
#         )

#         # Load initial local assets
#         self.refresh_local_assets()
#         self.page.add(self)
#         self.page.update()

#     def initialize_local_db(self):
#         cursor = self.local_db.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS assets (
#                 id INTEGER PRIMARY KEY,
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
#                 id INTEGER PRIMARY KEY,
#                 asset_id INTEGER,
#                 image_name TEXT,
#                 image_data BLOB,
#                 last_sync TEXT,
#                 FOREIGN KEY (asset_id) REFERENCES assets (id)
#             )
#         """)
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS asset_bills (
#                 id INTEGER PRIMARY KEY,
#                 asset_id INTEGER,
#                 bill_name TEXT,
#                 bill_data BLOB,
#                 last_sync TEXT,
#                 FOREIGN KEY (asset_id) REFERENCES assets (id)
#             )
#         """)
#         self.local_db.commit()

#     def refresh_local_assets(self):
#         cursor = self.local_db.cursor()
#         try:
#             cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status, last_sync FROM assets")
#             assets = cursor.fetchall()
#             print(f"SQLite3 query returned {len(assets)} assets: {[row[2] for row in assets]}")

#             self.local_asset_table.rows.clear()

#             if not assets:
#                 self.local_asset_table.rows.append(
#                     ft.DataRow(
#                         cells=[
#                             ft.DataCell(ft.Text("No local assets found in SQLite3.")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                         ]
#                     )
#                 )
#             else:
#                 for i, asset in enumerate(assets):
#                     asset_id, model, serial_number, company, location, purchase_date, status, last_sync = asset
#                     edit_button = ft.IconButton(
#                         icon=ft.Icons.EDIT,
#                         icon_color=ft.Colors.BLUE,
#                         bgcolor=ft.LinearGradient(
#                             begin=ft.alignment.top_left,
#                             end=ft.alignment.bottom_right,
#                             colors=[ft.Colors.BLUE_500, ft.Colors.BLUE_700]
#                         ),
#                         style=ft.ButtonStyle(
#                             shape=ft.RoundedRectangleBorder(radius=8),
#                             overlay_color=ft.Colors.BLUE_400
#                         ),
#                         tooltip="Edit Asset",
#                         on_click=lambda e, aid=asset_id: self.open_edit_dialog(aid)
#                     )
#                     self.local_asset_table.rows.append(
#                         ft.DataRow(
#                             cells=[
#                                 ft.DataCell(ft.Text(model or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Text(serial_number or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Text(location or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Container(content=edit_button, alignment=ft.alignment.center)),
#                             ],
#                             color=ft.Colors.WHITE if i % 2 == 0 else ft.Colors.BLUE_GREY_50
#                         )
#                     )

#             self.page.update()
#         except Exception as e:
#             print(f"Error fetching local asset data from SQLite3: {e}")
#             self.local_asset_table.rows.clear()
#             self.local_asset_table.rows.append(
#                 ft.DataRow(
#                     cells=[
#                         ft.DataCell(ft.Text(f"Error: {e}")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                     ]
#                 )
#             )
#             self.page.update()
#         finally:
#             cursor.close()

#     def sync_from_server(self, e):
#         db_config = {"host": "200.200.200.23", "user": "root", "password": "Pak@123", "database": "asm_sys"}
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             local_cursor = self.local_db.cursor()

#             local_cursor.execute("BEGIN TRANSACTION")
#             cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status FROM assets")
#             mysql_assets = cursor.fetchall()

#             for asset in mysql_assets:
#                 mysql_id, model, serial_number, company, location, purchase_date, status = asset
#                 local_cursor.execute("SELECT id FROM assets WHERE id = ?", (mysql_id,))
#                 existing_asset = local_cursor.fetchone()
#                 if existing_asset:
#                     local_id = mysql_id  # Use MySQL ID as the local ID
#                     local_cursor.execute("""
#                         UPDATE assets SET model = ?, company = ?, location = ?, purchase_date = ?, status = ?, last_sync = ?
#                         WHERE id = ?
#                     """, (model, company, location, purchase_date, status, time.strftime("%Y-%m-%d %H:%M:%S"), local_id))
#                 else:
#                     local_cursor.execute("""
#                         INSERT INTO assets (id, model, serial_number, company, location, purchase_date, status, last_sync)
#                         VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#                     """, (mysql_id, model, serial_number, company, location, purchase_date, status, time.strftime("%Y-%m-%d %H:%M:%S")))

#                 cursor.execute("SELECT id, asset_id, image_name, image_data FROM asset_images WHERE asset_id = %s", (mysql_id,))
#                 mysql_images = cursor.fetchall()
#                 local_cursor.execute("SELECT id, asset_id FROM asset_images WHERE asset_id = ?", (mysql_id,))
#                 existing_images = {row[0]: row[1] for row in local_cursor.fetchall()}
#                 for img in mysql_images:
#                     img_id, asset_id, image_name, image_data = img
#                     if img_id in existing_images:
#                         local_cursor.execute("""
#                             UPDATE asset_images SET image_name = ?, image_data = ?, last_sync = ? WHERE id = ?
#                         """, (image_name, image_data, time.strftime("%Y-%m-%d %H:%M:%S"), img_id))
#                     else:
#                         local_cursor.execute("""
#                             INSERT INTO asset_images (id, asset_id, image_name, image_data, last_sync)
#                             VALUES (?, ?, ?, ?, ?)
#                         """, (img_id, mysql_id, image_name, image_data, time.strftime("%Y-%m-%d %H:%M:%S")))

#                 cursor.execute("SELECT id, asset_id, bill_name, bill_data FROM asset_bills WHERE asset_id = %s", (mysql_id,))
#                 mysql_bills = cursor.fetchall()
#                 local_cursor.execute("SELECT id, asset_id FROM asset_bills WHERE asset_id = ?", (mysql_id,))
#                 existing_bills = {row[0]: row[1] for row in local_cursor.fetchall()}
#                 for bill in mysql_bills:
#                     bill_id, asset_id, bill_name, bill_data = bill
#                     if bill_id in existing_bills:
#                         local_cursor.execute("""
#                             UPDATE asset_bills SET bill_name = ?, bill_data = ?, last_sync = ? WHERE id = ?
#                         """, (bill_name, bill_data, time.strftime("%Y-%m-%d %H:%M:%S"), bill_id))
#                     else:
#                         local_cursor.execute("""
#                             INSERT INTO asset_bills (id, asset_id, bill_name, bill_data, last_sync)
#                             VALUES (?, ?, ?, ?, ?)
#                         """, (bill_id, mysql_id, bill_name, bill_data, time.strftime("%Y-%m-%d %H:%M:%S")))

#             self.local_db.commit()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text("Sync from server completed!"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#             self.refresh_local_assets()
#         except Error as e:
#             self.local_db.rollback()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Sync error: {e}"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#         finally:
#             if 'cursor' in locals():
#                 cursor.close()
#             if 'conn' in locals():
#                 conn.close()
#             if 'local_cursor' in locals():
#                 local_cursor.close()
#             self.page.update()

#     def sync_to_server(self, e):
#         db_config = {"host": "200.200.200.23", "user": "root", "password": "Pak@123", "database": "asm_sys"}
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             local_cursor = self.local_db.cursor()

#             cursor.execute("BEGIN")
#             local_cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status, last_sync FROM assets")
#             local_assets = local_cursor.fetchall()

#             for asset in local_assets:
#                 local_id, model, serial_number, company, location, purchase_date, status, last_sync = asset
#                 cursor.execute("SELECT id FROM assets WHERE id = %s", (local_id,))
#                 existing_asset = cursor.fetchone()
#                 if existing_asset:
#                     mysql_id = local_id  # Use local ID as the MySQL ID
#                     cursor.execute("""
#                         UPDATE assets SET model = %s, company = %s, location = %s, purchase_date = %s, status = %s
#                         WHERE id = %s
#                     """, (model, company, location, purchase_date, status, mysql_id))
#                 else:
#                     cursor.execute("""
#                         INSERT INTO assets (id, model, serial_number, company, location, purchase_date, status)
#                         VALUES (%s, %s, %s, %s, %s, %s, %s)
#                     """, (local_id, model, serial_number, company, location, purchase_date, status))
#                     mysql_id = local_id

#                 local_cursor.execute("SELECT id, asset_id, image_name, image_data, last_sync FROM asset_images WHERE asset_id = ?", (local_id,))
#                 images = local_cursor.fetchall()
#                 cursor.execute("SELECT id, image_name FROM asset_images WHERE asset_id = %s", (mysql_id,))
#                 existing_images = {row[0]: row[1] for row in cursor.fetchall()}
#                 for img in images:
#                     img_id, asset_id, image_name, image_data, last_sync = img
#                     if img_id in existing_images:
#                         cursor.execute("""
#                             UPDATE asset_images SET image_name = %s, image_data = %s WHERE id = %s AND asset_id = %s
#                         """, (image_name, image_data, img_id, mysql_id))
#                     else:
#                         cursor.execute("""
#                             INSERT INTO asset_images (id, asset_id, image_name, image_data)
#                             VALUES (%s, %s, %s, %s)
#                         """, (img_id, mysql_id, image_name, image_data))

#                 local_cursor.execute("SELECT id, asset_id, bill_name, bill_data, last_sync FROM asset_bills WHERE asset_id = ?", (local_id,))
#                 bills = local_cursor.fetchall()
#                 cursor.execute("SELECT id, bill_name FROM asset_bills WHERE asset_id = %s", (mysql_id,))
#                 existing_bills = {row[1]: row[0] for row in cursor.fetchall()}
#                 for bill in bills:
#                     bill_id, asset_id, bill_name, bill_data, last_sync = bill
#                     if bill_id in existing_bills:
#                         cursor.execute("""
#                             UPDATE asset_bills SET bill_data = %s WHERE id = %s
#                         """, (bill_data, bill_id))
#                     else:
#                         cursor.execute("""
#                             INSERT INTO asset_bills (id, asset_id, bill_name, bill_data)
#                             VALUES (%s, %s, %s, %s)
#                         """, (bill_id, mysql_id, bill_name, bill_data))

#             conn.commit()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text("Sync to server completed!"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#             self.refresh_local_assets()
#         except Error as e:
#             conn.rollback()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Sync error: {e}"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#         finally:
#             if 'cursor' in locals():
#                 cursor.close()
#             if 'conn' in locals():
#                 conn.close()
#             if 'local_cursor' in locals():
#                 local_cursor.close()
#             self.page.update()

#     def load_assets(self):
#         pass

#     def update_table(self):
#         pass

#     def open_edit_dialog(self, asset_id):
#         self.edit_dialog = AssetEditPage(self.page, self, asset_id=asset_id, local_db=self.local_db)
#         self.edit_dialog.open_dialog()



# import os
# os.environ["FLET_SECRET_KEY"] = "mysecret123"
# import flet as ft
# import mysql.connector
# from mysql.connector import Error
# import sqlite3
# from assetpage import AssetFormPage
# from assetedit import AssetEditPage
# import time

# class AssetPage(ft.Container):
#     def __init__(self, page: ft.Page):
#         super().__init__()

#         self.page = page
#         self.page.title = "Asset Management"
    
#         self.page.window.width = 365
#         self.page.window.height = 600
#         self.page.window.min_width = 360
#         self.page.window.min_height = 600
#         self.page.theme_mode = ft.ThemeMode.LIGHT
#         self.page.bgcolor = ft.Colors.WHITE

#         self.local_db = sqlite3.connect("assets.db", check_same_thread=False)
#         self.initialize_local_db()
        
#         self.add_asset_dialog = AssetFormPage(self.page, self, local_db=self.local_db)
        
#         self.page.appbar = ft.AppBar(
#             title=ft.Text("Asset Management", size=15, weight="bold"),
#             bgcolor=ft.Colors.GREEN_300,
#             color=ft.Colors.WHITE,
#             center_title=True,
#             automatically_imply_leading=False,
#         )

#         self.page.bottom_appbar = ft.BottomAppBar(
#             bgcolor=ft.Colors.BLUE,
#             shape=ft.NotchShape.CIRCULAR,
#             content=ft.Row(
#                 controls=[
#                     ft.PopupMenuButton(
#                         items=[
#                             ft.PopupMenuItem(text="Option 1"),
#                             ft.PopupMenuItem(text="Option 2"),
#                             ft.PopupMenuItem(text="Option 3"),
#                             ft.PopupMenuItem(text="Option 4"),
#                         ],
#                         icon=ft.Icon(ft.Icons.MENU_BOOK, color=ft.Colors.WHITE),
#                         tooltip="Menu Options",
#                     ),
#                     ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE, tooltip="Search"),
#                     ft.Container(expand=True),
#                     ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE, tooltip="Favorites"),
#                 ],
#             ),
#         )

#         self.expand = True
#         self.asset_add = []

#         self.add_asset_button = ft.ElevatedButton(
#             text="Add Asset",
#             icon=ft.Icons.ADD,
#             bgcolor=ft.Colors.TEAL_600,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#         )

#         self.Home_button = ft.ElevatedButton(
#             text="HOME",
#             icon=ft.Icons.HOME,
#             bgcolor=ft.Colors.GREEN_400,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.page.go("/"),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#         )

#         # Initialize local asset table with selected columns
#         self.local_asset_table = ft.DataTable(
#             columns=[
#                 ft.DataColumn(ft.Text("Model", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Serial Number", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Location", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Edit", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#             ],
#             rows=[],
#             border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#             vertical_lines=ft.border.BorderSide(1, ft.Colors.BLUE_GREY_300),
#             column_spacing=5,
#         )

#         self.sync_from_server_button = ft.ElevatedButton(
#             text="Sync from Server",
#             icon=ft.Icons.DOWNLOAD,
#             bgcolor=ft.Colors.PURPLE_500,
#             color=ft.Colors.WHITE,
#             on_click=self.sync_from_server,
#             width=150,
#             height=40,
#         )

#         self.sync_to_server_button = ft.ElevatedButton(
#             text="Sync to Server",
#             icon=ft.Icons.UPLOAD,
#             bgcolor=ft.Colors.PINK_500,
#             color=ft.Colors.WHITE,
#             on_click=self.sync_to_server,
#             width=150,
#             height=40,
#         )

#         self.content = ft.Container(
#             content=ft.Column(
#                 controls=[
#                     ft.Row(
#                         controls=[self.Home_button, self.add_asset_button],
#                         alignment=ft.MainAxisAlignment.START,
#                         spacing=10,
#                     ),
#                     ft.Text("Local Assets", size=18, weight=ft.FontWeight.BOLD),
#                     ft.Container(
#                         content=self.local_asset_table,
#                         expand=True,
#                         width=self.page.window.width - 20,
#                         clip_behavior=ft.ClipBehavior.HARD_EDGE,
#                         padding=5,
#                         border_radius=10,
#                         bgcolor=ft.Colors.LIGHT_BLUE_100,
#                         border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#                     ),
#                     ft.Row(
#                         controls=[self.sync_from_server_button, self.sync_to_server_button],
#                         alignment=ft.MainAxisAlignment.CENTER,
#                         spacing=10,
#                     ),
#                 ],
#                 expand=True,
#                 spacing=10,
#                 scroll=ft.ScrollMode.AUTO,
#             ),
#             padding=10,
#         )

#         # Load initial local assets
#         self.refresh_local_assets()
#         self.page.add(self)
#         self.page.update()

#     def initialize_local_db(self):
#         cursor = self.local_db.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS assets (
#                 id INTEGER PRIMARY KEY,
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
#                 id INTEGER PRIMARY KEY,
#                 asset_id INTEGER,
#                 image_name TEXT,
#                 image_data BLOB,
#                 last_sync TEXT,
#                 FOREIGN KEY (asset_id) REFERENCES assets (id)
#             )
#         """)
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS asset_bills (
#                 id INTEGER PRIMARY KEY,
#                 asset_id INTEGER,
#                 bill_name TEXT,
#                 bill_data BLOB,
#                 last_sync TEXT,
#                 FOREIGN KEY (asset_id) REFERENCES assets (id)
#             )
#         """)
#         self.local_db.commit()

#     def refresh_local_assets(self):
#         cursor = self.local_db.cursor()
#         try:
#             cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status, last_sync FROM assets")
#             assets = cursor.fetchall()
#             print(f"SQLite3 query returned {len(assets)} assets: {[row[2] for row in assets]}")

#             self.local_asset_table.rows.clear()

#             if not assets:
#                 self.local_asset_table.rows.append(
#                     ft.DataRow(
#                         cells=[
#                             ft.DataCell(ft.Text("No local assets found in SQLite3.")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                         ]
#                     )
#                 )
#             else:
#                 for i, asset in enumerate(assets):
#                     asset_id, model, serial_number, company, location, purchase_date, status, last_sync = asset
#                     edit_button = ft.IconButton(
#                         icon=ft.Icons.EDIT,
#                         icon_color=ft.Colors.BLUE,
#                         bgcolor=ft.LinearGradient(
#                             begin=ft.alignment.top_left,
#                             end=ft.alignment.bottom_right,
#                             colors=[ft.Colors.BLUE_500, ft.Colors.BLUE_700]
#                         ),
#                         style=ft.ButtonStyle(
#                             shape=ft.RoundedRectangleBorder(radius=8),
#                             overlay_color=ft.Colors.BLUE_400
#                         ),
#                         tooltip="Edit Asset",
#                         on_click=lambda e, aid=asset_id: self.open_edit_dialog(aid)
#                     )
#                     self.local_asset_table.rows.append(
#                         ft.DataRow(
#                             cells=[
#                                 ft.DataCell(ft.Text(model or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Text(serial_number or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Text(location or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Container(content=edit_button, alignment=ft.alignment.center)),
#                             ],
#                             color=ft.Colors.WHITE if i % 2 == 0 else ft.Colors.BLUE_GREY_50
#                         )
#                     )

#             self.page.update()
#         except Exception as e:
#             print(f"Error fetching local asset data from SQLite3: {e}")
#             self.local_asset_table.rows.clear()
#             self.local_asset_table.rows.append(
#                 ft.DataRow(
#                     cells=[
#                         ft.DataCell(ft.Text(f"Error: {e}")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                     ]
#                 )
#             )
#             self.page.update()
#         finally:
#             cursor.close()

#     def sync_from_server(self, e):
#         db_config = {"host": "200.200.200.23", "user": "root", "password": "Pak@123", "database": "asm_sys"}
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             local_cursor = self.local_db.cursor()

#             local_cursor.execute("BEGIN TRANSACTION")
#             cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status FROM assets")
#             mysql_assets = cursor.fetchall()

#             for asset in mysql_assets:
#                 mysql_id, model, serial_number, company, location, purchase_date, status = asset
#                 local_cursor.execute("SELECT id FROM assets WHERE id = ?", (mysql_id,))
#                 existing_asset = local_cursor.fetchone()
#                 if existing_asset:
#                     local_id = mysql_id
#                     local_cursor.execute("""
#                         UPDATE assets SET model = ?, company = ?, location = ?, purchase_date = ?, status = ?, last_sync = ?
#                         WHERE id = ?
#                     """, (model, company, location, purchase_date, status, time.strftime("%Y-%m-%d %H:%M:%S"), local_id))
#                 else:
#                     local_cursor.execute("""
#                         INSERT INTO assets (id, model, serial_number, company, location, purchase_date, status, last_sync)
#                         VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#                     """, (mysql_id, model, serial_number, company, location, purchase_date, status, time.strftime("%Y-%m-%d %H:%M:%S")))

#                 cursor.execute("SELECT id, asset_id, image_name, image_data FROM asset_images WHERE asset_id = %s", (mysql_id,))
#                 mysql_images = cursor.fetchall()
#                 local_cursor.execute("SELECT id, asset_id FROM asset_images WHERE asset_id = ?", (mysql_id,))
#                 existing_images = {row[0]: row[1] for row in local_cursor.fetchall()}
#                 for img in mysql_images:
#                     img_id, asset_id, image_name, image_data = img
#                     if img_id in existing_images:
#                         local_cursor.execute("""
#                             UPDATE asset_images SET image_name = ?, image_data = ?, last_sync = ? WHERE id = ?
#                         """, (image_name, image_data, time.strftime("%Y-%m-%d %H:%M:%S"), img_id))
#                     else:
#                         local_cursor.execute("""
#                             INSERT INTO asset_images (id, asset_id, image_name, image_data, last_sync)
#                             VALUES (?, ?, ?, ?, ?)
#                         """, (img_id, mysql_id, image_name, image_data, time.strftime("%Y-%m-%d %H:%M:%S")))

#                 cursor.execute("SELECT id, asset_id, bill_name, bill_data FROM asset_bills WHERE asset_id = %s", (mysql_id,))
#                 mysql_bills = cursor.fetchall()
#                 local_cursor.execute("SELECT id, asset_id FROM asset_bills WHERE asset_id = ?", (mysql_id,))
#                 existing_bills = {row[0]: row[1] for row in local_cursor.fetchall()}
#                 for bill in mysql_bills:
#                     bill_id, asset_id, bill_name, bill_data = bill
#                     if bill_id in existing_bills:
#                         local_cursor.execute("""
#                             UPDATE asset_bills SET bill_name = ?, bill_data = ?, last_sync = ? WHERE id = ?
#                         """, (bill_name, bill_data, time.strftime("%Y-%m-%d %H:%M:%S"), bill_id))
#                     else:
#                         local_cursor.execute("""
#                             INSERT INTO asset_bills (id, asset_id, bill_name, bill_data, last_sync)
#                             VALUES (?, ?, ?, ?, ?)
#                         """, (bill_id, mysql_id, bill_name, bill_data, time.strftime("%Y-%m-%d %H:%M:%S")))

#             self.local_db.commit()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text("Sync from server completed!"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#             self.refresh_local_assets()
#         except Error as e:
#             self.local_db.rollback()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Sync error: {e}"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#         finally:
#             if 'cursor' in locals():
#                 cursor.close()
#             if 'conn' in locals():
#                 conn.close()
#             if 'local_cursor' in locals():
#                 local_cursor.close()
#             self.page.update()

#     def sync_to_server(self, e):
#         db_config = {"host": "200.200.200.23", "user": "root", "password": "Pak@123", "database": "asm_sys"}
#         try:
#             conn = mysql.connector.connect(**db_config)
#             cursor = conn.cursor()
#             local_cursor = self.local_db.cursor()

#             cursor.execute("BEGIN")
#             local_cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status, last_sync FROM assets")
#             local_assets = local_cursor.fetchall()

#             for asset in local_assets:
#                 local_id, model, serial_number, company, location, purchase_date, status, last_sync = asset
#                 cursor.execute("SELECT id FROM assets WHERE id = %s", (local_id,))
#                 existing_asset = cursor.fetchone()
#                 if existing_asset:
#                     mysql_id = local_id
#                     cursor.execute("""
#                         UPDATE assets SET model = %s, company = %s, location = %s, purchase_date = %s, status = %s
#                         WHERE id = %s
#                     """, (model, company, location, purchase_date, status, mysql_id))
#                 else:
#                     cursor.execute("""
#                         INSERT INTO assets (id, model, serial_number, company, location, purchase_date, status)
#                         VALUES (%s, %s, %s, %s, %s, %s, %s)
#                     """, (local_id, model, serial_number, company, location, purchase_date, status))
#                     mysql_id = local_id

#                 local_cursor.execute("SELECT id, asset_id, image_name, image_data, last_sync FROM asset_images WHERE asset_id = ?", (local_id,))
#                 images = local_cursor.fetchall()
#                 cursor.execute("SELECT id, image_name FROM asset_images WHERE asset_id = %s", (mysql_id,))
#                 existing_images = {row[0]: row[1] for row in cursor.fetchall()}
#                 for img in images:
#                     img_id, asset_id, image_name, image_data, last_sync = img
#                     if img_id in existing_images:
#                         cursor.execute("""
#                             UPDATE asset_images SET image_name = %s, image_data = %s WHERE id = %s AND asset_id = %s
#                         """, (image_name, image_data, img_id, mysql_id))
#                     else:
#                         cursor.execute("""
#                             INSERT INTO asset_images (id, asset_id, image_name, image_data)
#                             VALUES (%s, %s, %s, %s)
#                         """, (img_id, mysql_id, image_name, image_data))

#                 local_cursor.execute("SELECT id, asset_id, bill_name, bill_data, last_sync FROM asset_bills WHERE asset_id = ?", (local_id,))
#                 bills = local_cursor.fetchall()
#                 cursor.execute("SELECT id, bill_name FROM asset_bills WHERE asset_id = %s", (mysql_id,))
#                 existing_bills = {row[0]: row[1] for row in cursor.fetchall()}  # Use id as key
#                 for bill in bills:
#                     bill_id, asset_id, bill_name, bill_data, last_sync = bill
#                     if bill_id in existing_bills:
#                         cursor.execute("""
#                             UPDATE asset_bills SET bill_name = %s, bill_data = %s WHERE id = %s AND asset_id = %s
#                         """, (bill_name, bill_data, bill_id, mysql_id))
#                     else:
#                         cursor.execute("""
#                             INSERT INTO asset_bills (id, asset_id, bill_name, bill_data)
#                             VALUES (%s, %s, %s, %s)
#                         """, (bill_id, mysql_id, bill_name, bill_data))

#             conn.commit()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text("Sync to server completed!"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#             self.refresh_local_assets()
#         except Error as e:
#             conn.rollback()
#             self.page.snack_bar = ft.SnackBar(
#                 content=ft.Text(f"Sync error: {e}"),
#                 duration=4000
#             )
#             self.page.snack_bar.open = True
#         finally:
#             if 'cursor' in locals():
#                 cursor.close()
#             if 'conn' in locals():
#                 conn.close()
#             if 'local_cursor' in locals():
#                 local_cursor.close()
#             self.page.update()

#     def load_assets(self):
#         pass

#     def update_table(self):
#         pass

#     def open_edit_dialog(self, asset_id):
#         self.edit_dialog = AssetEditPage(self.page, self, asset_id=asset_id, local_db=self.local_db)
#         self.edit_dialog.open_dialog()



# import os
# import flet as ft
# import sqlite3  
# from assetpage import AssetFormPage
# from assetedit import AssetEditPage
# from sync_server import initialize_local_db, sync_from_server, sync_to_server

# class AssetPage(ft.Container):
#     def __init__(self, page: ft.Page):
#         super().__init__()

#         self.page = page
#         self.page.title = "Asset Management"
    
#         self.page.window.width = 365
#         self.page.window.height = 600
#         self.page.window.min_width = 360
#         self.page.window.min_height = 600
#         self.page.theme_mode = ft.ThemeMode.LIGHT
#         self.page.bgcolor = ft.Colors.WHITE

#         self.local_db = sqlite3.connect("assets.db", check_same_thread=False)
#         initialize_local_db(self.local_db)
        
#         self.add_asset_dialog = AssetFormPage(self.page, self, local_db=self.local_db)
        
#         self.page.appbar = ft.AppBar(
#             title=ft.Text("Asset Management", size=15, weight="bold"),
#             bgcolor=ft.Colors.GREEN_300,
#             color=ft.Colors.WHITE,
#             center_title=True,
#             automatically_imply_leading=False,
#         )

#         self.page.bottom_appbar = ft.BottomAppBar(
#             bgcolor=ft.Colors.BLUE,
#             shape=ft.NotchShape.CIRCULAR,
#             content=ft.Row(
#                 controls=[
#                     ft.PopupMenuButton(
#                         items=[
#                             ft.PopupMenuItem(text="Option 1"),
#                             ft.PopupMenuItem(text="Option 2"),
#                             ft.PopupMenuItem(text="Option 3"),
#                             ft.PopupMenuItem(text="Option 4"),
#                         ],
#                         icon=ft.Icon(ft.Icons.MENU_BOOK, color=ft.Colors.WHITE),
#                         tooltip="Menu Options",
#                     ),
#                     ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE, tooltip="Search"),
#                     ft.Container(expand=True),
#                     ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE, tooltip="Favorites"),
#                 ],
#             ),
#         )

#         self.expand = True
#         self.asset_add = []

#         self.add_asset_button = ft.ElevatedButton(
#             text="Add Asset",
#             icon=ft.Icons.ADD,
#             bgcolor=ft.Colors.TEAL_600,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#         )

#         self.Home_button = ft.ElevatedButton(
#             text="HOME",
#             icon=ft.Icons.HOME,
#             bgcolor=ft.Colors.GREEN_400,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.page.go("/"),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#         )

#         # Initialize local asset table with selected columns
#         self.local_asset_table = ft.DataTable(
#             columns=[
#                 ft.DataColumn(ft.Text("Model", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Serial Number", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Location", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Edit", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#             ],
#             rows=[],
#             border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#             vertical_lines=ft.border.BorderSide(1, ft.Colors.BLUE_GREY_300),
#             column_spacing=5,
#         )

#         self.sync_from_server_button = ft.ElevatedButton(
#             text="Sync from Server",
#             icon=ft.Icons.DOWNLOAD,
#             bgcolor=ft.Colors.PURPLE_500,
#             color=ft.Colors.WHITE,
#             on_click=lambda e: sync_from_server(self.local_db, self.page),
#             width=150,
#             height=40,
#         )

#         self.sync_to_server_button = ft.ElevatedButton(
#             text="Sync to Server",
#             icon=ft.Icons.UPLOAD,
#             bgcolor=ft.Colors.PINK_500,
#             color=ft.Colors.WHITE,
#             on_click=lambda e: sync_to_server(self.local_db, self.page),
#             width=150,
#             height=40,
#         )

#         self.content = ft.Container(
#             content=ft.Column(
#                 controls=[
#                     ft.Row(
#                         controls=[self.Home_button, self.add_asset_button],
#                         alignment=ft.MainAxisAlignment.START,
#                         spacing=10,
#                     ),
#                     ft.Text("Local Assets", size=18, weight=ft.FontWeight.BOLD),
#                     ft.Container(
#                         content=self.local_asset_table,
#                         expand=True,
#                         width=self.page.window.width - 20,
#                         clip_behavior=ft.ClipBehavior.HARD_EDGE,
#                         padding=5,
#                         border_radius=10,
#                         bgcolor=ft.Colors.LIGHT_BLUE_100,
#                         border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#                     ),
#                     ft.Row(
#                         controls=[self.sync_from_server_button, self.sync_to_server_button],
#                         alignment=ft.MainAxisAlignment.CENTER,
#                         spacing=10,
#                     ),
#                 ],
#                 expand=True,
#                 spacing=10,
#                 scroll=ft.ScrollMode.AUTO,
#             ),
#             padding=10,
#         )

#         # Load initial local assets
#         self.refresh_local_assets()
#         self.page.add(self)
#         self.page.update()

#     def refresh_local_assets(self):
#         cursor = self.local_db.cursor()
#         try:
#             cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status, last_sync FROM assets")
#             assets = cursor.fetchall()
#             print(f"SQLite3 query returned {len(assets)} assets: {[row[2] for row in assets]}")

#             self.local_asset_table.rows.clear()

#             if not assets:
#                 self.local_asset_table.rows.append(
#                     ft.DataRow(
#                         cells=[
#                             ft.DataCell(ft.Text("No local assets found in SQLite3.")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                         ]
#                     )
#                 )
#             else:
#                 for i, asset in enumerate(assets):
#                     asset_id, model, serial_number, company, location, purchase_date, status, last_sync = asset
#                     edit_button = ft.IconButton(
#                         icon=ft.Icons.EDIT,
#                         icon_color=ft.Colors.BLUE,
#                         bgcolor=ft.LinearGradient(
#                             begin=ft.alignment.top_left,
#                             end=ft.alignment.bottom_right,
#                             colors=[ft.Colors.BLUE_500, ft.Colors.BLUE_700]
#                         ),
#                         style=ft.ButtonStyle(
#                             shape=ft.RoundedRectangleBorder(radius=8),
#                             overlay_color=ft.Colors.BLUE_400
#                         ),
#                         tooltip="Edit Asset",
#                         on_click=lambda e, aid=asset_id: self.open_edit_dialog(aid)
#                     )
#                     self.local_asset_table.rows.append(
#                         ft.DataRow(
#                             cells=[
#                                 ft.DataCell(ft.Text(model or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Text(serial_number or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Text(location or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Container(content=edit_button, alignment=ft.alignment.center)),
#                             ],
#                             color=ft.Colors.WHITE if i % 2 == 0 else ft.Colors.BLUE_GREY_50
#                         )
#                     )

#             self.page.update()
#         except Exception as e:
#             print(f"Error fetching local asset data from SQLite3: {e}")
#             self.local_asset_table.rows.clear()
#             self.local_asset_table.rows.append(
#                 ft.DataRow(
#                     cells=[
#                         ft.DataCell(ft.Text(f"Error: {e}")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                     ]
#                 )
#             )
#             self.page.update()
#         finally:
#             cursor.close()

#     def sync_from_server(self, e):
#         pass  # Handled by sync_server.py

#     def sync_to_server(self, e):
#         pass  # Handled by sync_server.py

#     def load_assets(self):
#         pass

#     def update_table(self):
#         pass

#     def open_edit_dialog(self, asset_id):
#         self.edit_dialog = AssetEditPage(self.page, self, asset_id=asset_id, local_db=self.local_db)
#         self.edit_dialog.open_dialog()




# import os
# import flet as ft
# import sqlite3
# from assetpage import AssetFormPage
# from assetedit import AssetEditPage
# from sync_server import initialize_local_db, sync_from_server, sync_to_server

# class AssetPage(ft.Container):
#     def __init__(self, page: ft.Page):
#         super().__init__()

#         self.page = page
#         self.page.title = "Asset Management"
    
#         self.page.window.width = 365
#         self.page.window.height = 600
#         self.page.window.min_width = 360
#         self.page.window.min_height = 600
#         self.page.theme_mode = ft.ThemeMode.LIGHT
#         self.page.bgcolor = ft.Colors.WHITE

#         self.local_db = sqlite3.connect("assets.db", check_same_thread=False)
#         initialize_local_db(self.local_db)
        
#         self.add_asset_dialog = AssetFormPage(self.page, self, local_db=self.local_db)
        
#         self.page.appbar = ft.AppBar(
#             title=ft.Text("Asset Management", size=15, weight="bold"),
#             bgcolor=ft.Colors.GREEN_300,
#             color=ft.Colors.WHITE,
#             center_title=True,
#             automatically_imply_leading=False,
#         )

#         self.page.bottom_appbar = ft.BottomAppBar(
#             bgcolor=ft.Colors.BLUE,
#             shape=ft.NotchShape.CIRCULAR,
#             content=ft.Row(
#                 controls=[
#                     ft.PopupMenuButton(
#                         items=[
#                             ft.PopupMenuItem(text="Option 1"),
#                             ft.PopupMenuItem(text="Option 2"),
#                             ft.PopupMenuItem(text="Option 3"),
#                             ft.PopupMenuItem(text="Option 4"),
#                         ],
#                         icon=ft.Icon(ft.Icons.MENU_BOOK, color=ft.Colors.WHITE),
#                         tooltip="Menu Options",
#                     ),
#                     ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE, tooltip="Search"),
#                     ft.Container(expand=True),
#                     ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE, tooltip="Favorites"),
#                 ],
#             ),
#         )

#         self.expand = True
#         self.asset_add = []

#         self.add_asset_button = ft.ElevatedButton(
#             text="Add Asset",
#             icon=ft.Icons.ADD,
#             bgcolor=ft.Colors.TEAL_600,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.add_asset_dialog.open_dialog(),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#         )

#         self.Home_button = ft.ElevatedButton(
#             text="HOME",
#             icon=ft.Icons.HOME,
#             bgcolor=ft.Colors.GREEN_400,
#             color=ft.Colors.WHITE,
#             elevation=4,
#             on_click=lambda e: self.page.go("/"),
#             style=ft.ButtonStyle(
#                 shape=ft.RoundedRectangleBorder(radius=12),
#                 overlay_color=ft.Colors.TEAL_700
#             ),
#             width=120,
#             height=40,
#         )

#         # Initialize local asset table with selected columns
#         self.local_asset_table = ft.DataTable(
#             columns=[
#                 ft.DataColumn(ft.Text("Model", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Serial Number", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Location", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#                 ft.DataColumn(ft.Text("Edit", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
#             ],
#             rows=[],
#             border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#             vertical_lines=ft.border.BorderSide(1, ft.Colors.BLUE_GREY_300),
#             column_spacing=5,
#         )

#         self.sync_from_server_button = ft.ElevatedButton(
#             text="Sync from Server",
#             icon=ft.Icons.DOWNLOAD,
#             bgcolor=ft.Colors.PURPLE_500,
#             color=ft.Colors.WHITE,
#             on_click=lambda e: self.sync_from_server(),
#             width=150,
#             height=40,
#         )

#         self.sync_to_server_button = ft.ElevatedButton(
#             text="Sync to Server",
#             icon=ft.Icons.UPLOAD,
#             bgcolor=ft.Colors.PINK_500,
#             color=ft.Colors.WHITE,
#             on_click=lambda e: self.sync_to_server(),
#             width=150,
#             height=40,
#         )

#         # AlertDialog for sync operations
#         self.sync_dialog = ft.AlertDialog(
#             modal=True,
#             title=ft.Text("Sync Status"),
#             content=ft.Text(""),
#             actions=[ft.TextButton("OK", on_click=self.close_sync_dialog)],
#             actions_alignment=ft.MainAxisAlignment.END
#         )
#         self.page.overlay.append(self.sync_dialog)

#         self.content = ft.Container(
#             content=ft.Column(
#                 controls=[
#                     ft.Row(
#                         controls=[self.Home_button, self.add_asset_button],
#                         alignment=ft.MainAxisAlignment.START,
#                         spacing=10,
#                     ),
#                     ft.Text("Local Assets", size=18, weight=ft.FontWeight.BOLD),
#                     ft.Container(
#                         content=self.local_asset_table,
#                         expand=True,
#                         width=self.page.window.width - 20,
#                         clip_behavior=ft.ClipBehavior.HARD_EDGE,
#                         padding=5,
#                         border_radius=10,
#                         bgcolor=ft.Colors.LIGHT_BLUE_100,
#                         border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
#                     ),
#                     ft.Row(
#                         controls=[self.sync_from_server_button, self.sync_to_server_button],
#                         alignment=ft.MainAxisAlignment.CENTER,
#                         spacing=10,
#                     ),
#                 ],
#                 expand=True,
#                 spacing=10,
#                 scroll=ft.ScrollMode.AUTO,
#             ),
#             padding=10,
#         )

#         # Load initial local assets
#         self.refresh_local_assets()
#         self.page.add(self)
#         self.page.update()

#     def refresh_local_assets(self):
#         cursor = self.local_db.cursor()
#         try:
#             cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status, last_sync FROM assets")
#             assets = cursor.fetchall()
#             print(f"SQLite3 query returned {len(assets)} assets: {[row[2] for row in assets]}")

#             self.local_asset_table.rows.clear()

#             if not assets:
#                 self.local_asset_table.rows.append(
#                     ft.DataRow(
#                         cells=[
#                             ft.DataCell(ft.Text("No local assets found in SQLite3.")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                             ft.DataCell(ft.Text("")),
#                         ]
#                     )
#                 )
#             else:
#                 for i, asset in enumerate(assets):
#                     asset_id, model, serial_number, company, location, purchase_date, status, last_sync = asset
#                     edit_button = ft.IconButton(
#                         icon=ft.Icons.EDIT,
#                         icon_color=ft.Colors.BLUE,
#                         bgcolor=ft.LinearGradient(
#                             begin=ft.alignment.top_left,
#                             end=ft.alignment.bottom_right,
#                             colors=[ft.Colors.BLUE_500, ft.Colors.BLUE_700]
#                         ),
#                         style=ft.ButtonStyle(
#                             shape=ft.RoundedRectangleBorder(radius=8),
#                             overlay_color=ft.Colors.BLUE_400
#                         ),
#                         tooltip="Edit Asset",
#                         on_click=lambda e, aid=asset_id: self.open_edit_dialog(aid)
#                     )
#                     self.local_asset_table.rows.append(
#                         ft.DataRow(
#                             cells=[
#                                 ft.DataCell(ft.Text(model or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Text(serial_number or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Text(location or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
#                                 ft.DataCell(ft.Container(content=edit_button, alignment=ft.alignment.center)),
#                             ],
#                             color=ft.Colors.WHITE if i % 2 == 0 else ft.Colors.BLUE_GREY_50
#                         )
#                     )

#             self.page.update()
#         except Exception as e:
#             print(f"Error fetching local asset data from SQLite3: {e}")
#             self.local_asset_table.rows.clear()
#             self.local_asset_table.rows.append(
#                 ft.DataRow(
#                     cells=[
#                         ft.DataCell(ft.Text(f"Error: {e}")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                         ft.DataCell(ft.Text("")),
#                     ]
#                 )
#             )
#             self.page.update()
#         finally:
#             cursor.close()

#     def sync_from_server(self, e=None):
#         sync_from_server(self.local_db, self.page)
#         self.sync_dialog.content = ft.Text("Sync from server completed!")
#         self.sync_dialog.open = True
#         self.page.update()

#     def sync_to_server(self, e=None):
#         sync_to_server(self.local_db, self.page)
#         self.sync_dialog.content = ft.Text("Sync to server completed!")
#         self.sync_dialog.open = True
#         self.page.update()

#     def close_sync_dialog(self, e):
#         self.sync_dialog.open = False
#         self.page.update()

#     def load_assets(self):
#         pass

#     def update_table(self):
#         pass

#     def open_edit_dialog(self, asset_id):
#         self.edit_dialog = AssetEditPage(self.page, self, asset_id=asset_id, local_db=self.local_db)
#         self.edit_dialog.open_dialog()




import os
import flet as ft
import sqlite3
from assetpage import AssetFormPage
from assetedit import AssetEditPage
from sync_server import initialize_local_db, sync_from_server, sync_to_server

class AssetPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page
        self.page.title = "Asset Management"
    
        self.page.window.width = 365
        self.page.window.height = 600
        self.page.window.min_width = 360
        self.page.window.min_height = 600
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.bgcolor = ft.Colors.WHITE

        self.local_db = sqlite3.connect("assets.db", check_same_thread=False)
        initialize_local_db(self.local_db)
        
        self.add_asset_dialog = AssetFormPage(self.page, self, local_db=self.local_db)
        
        self.page.appbar = ft.AppBar(
            title=ft.Text("Asset Management", size=15, weight="bold"),
            bgcolor=ft.Colors.GREEN_300,
            color=ft.Colors.WHITE,
            center_title=True,
            automatically_imply_leading=False,
        )

        self.page.bottom_appbar = ft.BottomAppBar(
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

        self.expand = True
        self.asset_add = []

        self.add_asset_button = ft.ElevatedButton(
            text="Add Asset",
            icon=ft.Icons.ADD,
            bgcolor=ft.Colors.TEAL_600,
            color=ft.Colors.WHITE,
            elevation=4,
            on_click=lambda e: self.add_asset_dialog.open_dialog(),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=12),
                overlay_color=ft.Colors.TEAL_700
            ),
            width=120,
            height=40,
        )

        self.Home_button = ft.ElevatedButton(
            text="HOME",
            icon=ft.Icons.HOME,
            bgcolor=ft.Colors.GREEN_400,
            color=ft.Colors.WHITE,
            elevation=4,
            on_click=lambda e: self.page.go("/"),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=12),
                overlay_color=ft.Colors.TEAL_700
            ),
            width=120,
            height=40,
        )

        # Initialize local asset table with selected columns
        self.local_asset_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Model", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
                ft.DataColumn(ft.Text("Serial Number", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
                ft.DataColumn(ft.Text("Location", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
                ft.DataColumn(ft.Text("Edit", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)),
            ],
            rows=[],
            border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
            vertical_lines=ft.border.BorderSide(1, ft.Colors.BLUE_GREY_300),
            column_spacing=5,
        )

        self.sync_from_server_button = ft.ElevatedButton(
            text="Sync from Server",
            icon=ft.Icons.DOWNLOAD,
            bgcolor=ft.Colors.PURPLE_500,
            color=ft.Colors.WHITE,
            on_click=lambda e: self.sync_from_server(),
            width=150,
            height=40,
        )

        self.sync_to_server_button = ft.ElevatedButton(
            text="Sync to Server",
            icon=ft.Icons.UPLOAD,
            bgcolor=ft.Colors.PINK_500,
            color=ft.Colors.WHITE,
            on_click=lambda e: self.sync_to_server(),
            width=150,
            height=40,
        )

        # AlertDialog for sync operations
        self.sync_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Sync Status"),
            content=ft.Text(""),
            actions=[ft.TextButton("OK", on_click=self.close_sync_dialog)],
            actions_alignment=ft.MainAxisAlignment.END
        )
        self.page.overlay.append(self.sync_dialog)

        self.content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[self.Home_button, self.add_asset_button],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10,
                    ),
                    ft.Text("Local Assets", size=18, weight=ft.FontWeight.BOLD),
                    ft.Container(
                        content=self.local_asset_table,
                        expand=True,
                        width=self.page.window.width - 20,
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                        padding=5,
                        border_radius=10,
                        bgcolor=ft.Colors.LIGHT_BLUE_100,
                        border=ft.border.all(1, ft.Colors.BLUE_GREY_300),
                    ),
                    ft.Row(
                        controls=[self.sync_from_server_button, self.sync_to_server_button],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                    ),
                ],
                expand=True,
                spacing=10,
                scroll=ft.ScrollMode.AUTO,
            ),
            padding=10,
        )

        # Load initial local assets
        self.refresh_local_assets()
        self.page.add(self)
        self.page.update()

    def refresh_local_assets(self):
        cursor = self.local_db.cursor()
        try:
            cursor.execute("SELECT id, model, serial_number, company, location, purchase_date, status, last_sync FROM assets")
            assets = cursor.fetchall()
            print(f"SQLite3 query returned {len(assets)} assets: {[row[2] for row in assets]}")

            self.local_asset_table.rows.clear()

            if not assets:
                self.local_asset_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("No local assets found in SQLite3.")),
                            ft.DataCell(ft.Text("")),
                            ft.DataCell(ft.Text("")),
                            ft.DataCell(ft.Text("")),
                        ]
                    )
                )
            else:
                for i, asset in enumerate(assets):
                    asset_id, model, serial_number, company, location, purchase_date, status, last_sync = asset
                    edit_button = ft.IconButton(
                        icon=ft.Icons.EDIT,
                        icon_color=ft.Colors.BLUE,
                        bgcolor=ft.LinearGradient(
                            begin=ft.alignment.top_left,
                            end=ft.alignment.bottom_right,
                            colors=[ft.Colors.BLUE_500, ft.Colors.BLUE_700]
                        ),
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=8),
                            overlay_color=ft.Colors.BLUE_400
                        ),
                        tooltip="Edit Asset",
                        on_click=lambda e, aid=asset_id: self.open_edit_dialog(aid)
                    )
                    self.local_asset_table.rows.append(
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text(model or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
                                ft.DataCell(ft.Text(serial_number or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
                                ft.DataCell(ft.Text(location or "N/A", color=ft.Colors.BLUE_GREY_800, size=12)),
                                ft.DataCell(ft.Container(content=edit_button, alignment=ft.alignment.center)),
                            ],
                            color=ft.Colors.WHITE if i % 2 == 0 else ft.Colors.BLUE_GREY_50
                        )
                    )

            self.page.update()
            print(f"Refreshed asset table with {len(self.local_asset_table.rows)} rows")
        except Exception as e:
            print(f"Error fetching local asset data from SQLite3: {e}")
            self.local_asset_table.rows.clear()
            self.local_asset_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(f"Error: {e}")),
                        ft.DataCell(ft.Text("")),
                        ft.DataCell(ft.Text("")),
                        ft.DataCell(ft.Text("")),
                    ]
                )
            )
            self.page.update()
        finally:
            cursor.close()

    def sync_from_server(self, e=None):
        sync_from_server(self.local_db, self.page)
        self.sync_dialog.content = ft.Text("Sync from server completed!")
        self.sync_dialog.open = True
        self.page.update()

    def sync_to_server(self, e=None):
        sync_to_server(self.local_db, self.page)
        self.sync_dialog.content = ft.Text("Sync to server completed!")
        self.sync_dialog.open = True
        self.page.update()

    def close_sync_dialog(self, e):
        self.sync_dialog.open = False
        self.page.update()

    def load_assets(self):
        pass

    def update_table(self):
        pass

    def open_edit_dialog(self, asset_id):
        self.edit_dialog = AssetEditPage(self.page, self, asset_id=asset_id, local_db=self.local_db)
        self.edit_dialog.open_dialog()