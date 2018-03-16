<template>
    <div>
     <el-dialog title="编辑项目" :visible.sync="editProjectFormVisible">
      <el-form :model="row">
        <el-form-item label="项目ID" :label-width="formLabelWidth">
          <el-input v-model="row.id" :disabled="true" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="项目名称" :label-width="formLabelWidth">
          <el-input v-model="row.project_name" auto-complete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="$parent.editProjectFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="handleEditProject">确 定</el-button>
      </div>
    </el-dialog>
    </div>
</template>

<script>
    import api from '../../api/api.js';
  export default {
    props: {
      editProjectFormVisible: {
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
        handleEditProject(){
            let self = this;
            self.$http.put(`${api.host}/projects/${this.row.id}/`, this.row)
            .then((response) => {
                self.$parent.getProjects();
            })
            self.$parent.editProjectFormVisible = false
        }
    }
  };
</script>

<style scoped>

</style>