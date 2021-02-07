**Habit Tracker GUI**

-- WIP --

Goal: to create a habit tracker app as a standalone .exe using guizero and PyInstaller for my own personal use. The 
app will assume that the user already exists and has already created a graph. A next step (someday) might be to add 
functionality to create users and graphs.

Current status: basic app functionality is complete. Captured data is error-checked before being passed to the API 
functions to reduce the chance of unsuccessful API requests. All three HTTP methods (add, modify, and delete) complete 
successfully with valid data.

Next steps:

- display the short version (~90 days) of a selected graph

- add the ability to create new users and graphs. Store users' API tokens (and graph IDs?) in a local file (JSON?).

- use PyInstaller to bundle the app into a standalone .exe