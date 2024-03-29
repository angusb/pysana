# pysana

Python wrapper for the [Asana v1 RESTful API](http://developer.asana.com/documentation/).

Note: This library is relatively new and subject to change. If you have ideas on how to improve it, please get in touch with me. 

## Example Usage

```python
from asana import Asana
api = Asana('123124.abcDeFg1234KlMNopQ56')
primary_workspace = api.find_workspace('Personal Projects')
my_tasks = primary_workspace.find_tasks(api.User())
```

## Documentation

This wrapper implementation takes an object oriented approach. It closely maps the resources Asana provides (workspaces, users, tags, etc..) into objects. 

### Creating the API Object:

**All calls to the API require instantiating an Asana object.** An Asana object is tied to a single user's API key. You can create an Asana object with a configuration file that looks like the following:
```
    [Asana Configuration]
    api_key = 123124.abcDeFg1234KlMNopQ56
    debug = false
```

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

### Working with AsanaResource Objects:

The following AsanaResource's exist:
* User
* Workspace
* Project
* Task
* Tag
* Story

Once you have an Asana object (api, above) you can use it to instantiate any of the above AsanaResources. Instantiating an Asana object does not *necessarily* imply that a new resource is created (e.g. Asana's API doesn't allow you to create new users or workspaces). 

Though you can create Asana Resource objects with IDs (see below), the following is more likely:

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

#### Asana:

Check the source code to determine what parameters each constructor can accept.

**Note:** every Asana object has an ID. It's very easy to use the id to create an AsanaResource object.

Constructors:
```python

w_id = '13315135'

api_user = api.User()
other_user = api.User('2966100')

existing_workspace = api.Workspace(w_id)

existing_tag = api.Tag('23596722')
new_tag = api.Tag(workspace_id=w_id, name='important', notes='code red')

existing_project = api.Project('55966708')
new_project = api.Project(workspace_id=w_id, name='Homework')

existing_task = api.Task('32511342')
new_task = api.Task(workspace_id=w_id,
                    name='Write Report',
                    assignee_status='later',
                    notes='Write nutrition report and Deliver to Bob',
                    assignee=other_user.id)

existing_story = api.Story('55679803')
```

Methods:
```python

tom = api.find_user('Tom Foolery')
important_tag = api.find_tag('Code Red')
personal = api.find_workspace('Personal Projects')
```

#### User:
<table>
  <tr>
    <th>Property</th><th>Type</th><th>Settable?</th>
  </tr>
  <tr>
    <td>id</td><td>int</td><td>--</td>
  </tr>
  <tr>
    <td>name</td><td>str</td><td>--</td>
  </tr>
  <tr>
    <td>email</td><td>str</td><td>--</td>
  </tr>
  <tr>
    <td>workspaces</td><td>list(Workspace)</td><td>--</td>
  </tr>
</table>


```python
# Create users that we can then interact with
myself = api.User('me') 
doug = api.User(1351325124) # 1351325124 is the user id of doug

my_workspaces = myself.workspaces
dougs_workspaces = doug.workspaces

# Shared workspace names between doug and myself
shared_workspaces = [mw.name for mw in my_workspaces.workspaces for dw in dougs_workspaces.workspaces if mw.name == dw.name]
```

## Todo
* Add to pip
* Handle TODO's in code
* Test coverage

## Contributing
* Send me an email or create an Issue of what you want to do
* Fork 
* Create a branch
* Commit and push to the newly created branch
* Submit a Pull Request
