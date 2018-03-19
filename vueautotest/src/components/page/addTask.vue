<template>
    <div>
     <el-dialog title="创建任务" :visible.sync="addTaskFormVisible">
      <el-form :model="row">
        <el-form-item label="项目ID" :label-width="formLabelWidth">
          <el-input v-model="projectId" :disabled="true" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="任务名称" :label-width="formLabelWidth">
          <el-input v-model="row.task_name" auto-complete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="$parent.addTaskFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="handleAddTask">确 定</el-button>
      </div>
    </el-dialog>
    </div>
</template>

<script>
    import api from '../../api/api.js';
  export default {
    props: {
      addTaskFormVisible: {
        type: Boolean
      },
      projectId: {
        type: Number
      },
    },
    data() {
      return {
        formLabelWidth: '120px',
        row: {
          projects: '',
          task_name:''
        }
      };
    },
    computed:{

    },
    created() {

    },
    methods: {
        handleAddTask(){
            let self = this;
            self.row = {projects: this.projectId, task_name: this.row.task_name};
            self.$http.post(`${api.host}/tasks/`, self.row)
            .then((response) => {
                self.$parent.handleTasks();
            })
            self.$parent.addTaskFormVisible = false
        }
    }
  };
</script>

<style>

</style>