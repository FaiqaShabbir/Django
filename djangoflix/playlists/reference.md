```python

class CorseGrade():
    student -> FK(Student)
    course -> FK(Course)

class CorseGAttendance():
    student -> FK(Student)
    course -> FK(Course)
    datetime -> DateTime()

class Course():
    students -> M2M()
    """below line will actually give me all of those grades for that course grade"""
    # course_obj.coursegrade_set.all()
    # course_obj.courseattendance_set.all(0)
class Parent():
    name
    # parent_obj.student_set.all()

class Student():
    mother = FK(Parent, related_name='mother')
    father = FK(Parent, related_name='father')
    # student.course_set.all()
    # student.coursegrade_set.all()
    # student.father
    # student.mother

```
playlist_a = Playlist.objects.first()
## Add To ManyToMany
```python
video_a = Video.objects.first()
playlist_a.videos.add(video_a)
```

## Remove To ManyToMany
```python
video_a = Video.objects.first()
playlist_a.videos.remove(video_a)
```

## Set (or reset) ManyToMany
```python
video_qs = Video.objects.all()
playlist_a.videos.set(video_qs)
```

## Clear ManyToMany
```python
playlist_a.videos.clear()
```

## Querset from ManyToMany
```python
playlist_a.videos.all()
```

## Playlists of Playlists
``` python
from playlists.models import Playlist

the_office = Playlist.objects.create(title='The Office Series')
# featured video / videos /

season_1 = Playlist.objects.create(title='The Office Series Season 1', parent=the_office, order=1)
# featured video / videos /

season_2 = Playlist.objects.create(title='The Office Series Season 2',
parent=the_office, order=2)
# featured video / videos /

season_3 = Playlist.objects.create(title='The Office Series Season 3',
parent=the_office, order=3)
# featured video / videos /
shows = Playlist.objects.filter(parent__isnull=True)
show = Playlist.objects.get(id=1)
# season = Playlist.objects.filter(parent=show)
```