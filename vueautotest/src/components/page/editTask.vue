<template>
    <div>
     <el-dialog title="编辑任务" :visible.sync="editTaskFormVisible">
      <el-form :model="row">
        <el-form-item label="任务ID" :label-width="formLabelWidth">
          <el-input v-model="row.id" :disabled="true" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="任务名称" :label-width="formLabelWidth">
          <el-input v-model="row.task_name" auto-complete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="$parent.editTaskFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="handleEditTask">确 定</el-button>
      </div>
    </el-dialog>
    </div>
</template>

<script>
    import api from '../../api/api.js';
  export default {
    props: {
      editTaskFormVisible: {
        type: Boolean
      },
      row: {
        type: Object
      },
    },
    data() {
      return {
        formLabelWidth: '120px'
      };
    },
    computed:{

    },
    methods: {
        handleEditTask(){
            let self = this;
            self.$http.put(`${api.host}/tasks/${this.row.id}/`, this.row)
            .then((response) => {
                self.$parent.handleTasks();
            })
            self.$parent.editTaskFormVisible = false
        }
    }
  };
</script>

<style scoped>

</style>