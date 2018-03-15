<template>
    <div>
     <el-dialog title="创建项目" :visible.sync="addProjectFormVisible">
      <el-form :model="row">
        <el-form-item label="用户ID" :label-width="formLabelWidth">
          <el-input v-model="row.user" :disabled="true" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="项目名称" :label-width="formLabelWidth">
          <el-input v-model="row.project_name" auto-complete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="$parent.addProjectFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="handleAddProject">确 定</el-button>
      </div>
    </el-dialog>
    </div>
</template>

<script>
    import api from '../../api/api.js';
  export default {
    props: {
      addProjectFormVisible: {
        type: Boolean
      },
    },
    data() {
      return {
        formLabelWidth: '120px',
        row: {
          user: localStorage.getItem("ms_userid"),
          project_name:''
        }
      };
    },
    computed:{

    },
    methods: {
        handleAddProject(){
            let self = this;
            self.$http.post(`${api.host}/projects/`, this.row)
            .then((response) => {
                self.$parent.getProjects();
            })
            self.$parent.addProjectFormVisible = false
        }
    }
  };
</script>

<style>

</style>