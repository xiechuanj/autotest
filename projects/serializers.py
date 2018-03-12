from rest_framework import serializers

from .models import Projects, User, Task, TaskSet, TaskRun, TaskSetRun, TaskInstance, Menus, TaskStatus


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = "__all__"

class TaskRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskRun
        fields = "__all__"

class TaskSetRunSerializer(serializers.ModelSerializer):
    taskruns = TaskRunSerializer(many=True, read_only=True)
    class Meta:
        model = TaskSetRun
        fields = "__all__"


class TaskInstanceSerializer(serializers.ModelSerializer):
    # tasksets = TaskRunSerializer(many=True)
    class Meta:
        model = TaskInstance
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    taskinstances = TaskInstanceSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = "__all__"

class TaskSetSerializer(serializers.ModelSerializer):
    taskinstances = TaskInstanceSerializer(many=True, read_only=True)
    tasksetruns = TaskSetRunSerializer(many=True, read_only=True)
    class Meta:
        model = TaskSet
        fields = "__all__"

class ProjectsSerializer(serializers.ModelSerializer):
    tasksets = TaskSetSerializer(many=True, read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Projects
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    projects = ProjectsSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'projects', 'email')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()
        return user


class MenuCategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = "__all__"

class MenuCategorySerializer2(serializers.ModelSerializer):
    sub_menu = MenuCategorySerializer3(many=True, read_only=True)
    class Meta:
        model = Menus
        fields = "__all__"

class MenusSerializer(serializers.ModelSerializer):
    sub_menu = MenuCategorySerializer2(many=True, read_only=True)
    class Meta:
        model = Menus
        fields = "__all__"
