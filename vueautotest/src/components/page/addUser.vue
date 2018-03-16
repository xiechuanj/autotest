<template>
    <div>
     <el-dialog title="创建用户" :visible.sync="addUserFormVisible">
      <el-form :model="user">
        <el-form-item label="用户名" :label-width="formLabelWidth">
          <el-input v-model="user.username"  auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="用户密码" :label-width="formLabelWidth">
          <el-input type="password" v-model="user.password" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" :label-width="formLabelWidth">
          <el-input v-model="user.email" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="超级用户" :label-width="formLabelWidth">
          <el-checkbox :disabled="true" v-model="user.is_superuser">是否超级用户</el-checkbox>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="$parent.addUserFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="handleAddProject">确 定</el-button>
      </div>
    </el-dialog>
    </div>
</template>

<script>
    import api from '../../api/api.js';
  export default {
    props: {
      addUserFormVisible: {
        type: Boolean
      },
    },
    data() {
      return {
        formLabelWidth: '120px',
        user: {
          username: "",
          password:"",
          email:"",
          is_superuser: false
        }
      };
    },
    computed:{

    },
    methods: {
        handleAddProject(){
            let self = this;
            self.$http.post(`${api.host}/api-register/`, this.user)
            .then((response) => {
                self.$parent.getUsers();
            })
            self.$parent.addUserFormVisible = false;
        }
    }
  };
</script>

<style>

</style>