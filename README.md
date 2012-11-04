# pysana

Python wrapper for the [Asana v1 API](http://developer.asana.com/documentation/)

Note: This library is relatively new and subject to change. If you have ideas on how to improve it, please get in touch with me. 

## Example Usage

```python
from asana import Asana
api = Asana('123124.abcDeFg1234KlMNopQ56')
me = api.User()
all_workspaces = api.workspaces
```

## Documentation

### Creating the API Object

All calls to the API require instantiating an Asana object. An Asana object is tied to a single user's API key. You can create an Asana object with a configuration file that looks like the following:
	[Asana Configuration]
	api_key = 123124.abcDeFg1234KlMNopQ56
	debug = false

Then you can pass in the file location:

```python
from asana import Asana
api = Asana(config_file='./asana.cfg') # Relative paths with '~' won't work.
```

Or pass the API key in directly:

```python
from asana import Asana
api = Asana('123124.abcDeFg1234KlMNopQ56', debug=False)
```

### Working with AsanaResource Objects

This wrapper implementation takes an object oriented approach. The following AsanaResource's exist:
* User
* Workspace
* Project
* Task
* Tag
* Story

Once you have an Asana object (api, above) you can use it to instantiate any of the above AsanaResources. Instantiating an Asana object does not *necessarily* imply that a new resource is created (e.g. Asana's API doesn't allow you to create new users or workspaces). 

Every Asana resouce has an id. It is very easy to create an object out of it once you have the ID.

```python
myself = api.User('135161039')
red_tag = api.Tag('395026900')
primary_workspace = api.Workspace('598703954')
due_today_tag = api.Tag('489694816')
# etc...
```

This method to create Asana Resource objects, however, is unlikely to be used. Here's more likely scenarios:

```python
## Self contained examples:

# 1.
personal_stuff = api.find_workspace('Personal Projects')
christmas_project = personal_stuff.create_project('Christmas Planning')
christimas_project.add_comment('Coming up quick!')

# 2.
work = api.find_workspace('Work')
task = work.create_task('Send draft to Kristen')
task.add_comment('Should be done soon...')
task.assignee_status = 'today'
subtask = task.add_subtask('Install Micrsoft Word')

# 3.
vacation = api.find_workspace('Vacation Planning')
hotels = vacation.find_tag('hotels')
remaining_hotel_tasks = [t for t in hotels.tasks if t.assignee_status == 'today']
```

```python
# Create users that we can then interact with
myself = api.User('me') 
doug = api.User(1351325124) # 1351325124 is the user id of doug

my_workspaces = myself.workspaces
dougs_workspaces = doug.workspaces

# Shared workspace names between doug and myself
shared_workspaces = [mw.name for mw in my_workspaces.workspaces for dw in dougs_workspaces.workspaces if mw.name == dw.name]
```

To obtain 

## Todo
* Add to pip
* Test coverage

## Contributing
* Fork 
* Create a branch
* Commit and push to the newly created branch
* Submit a Pull Request
