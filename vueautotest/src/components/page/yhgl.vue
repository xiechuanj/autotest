<template>
    <div class="table">
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-menu"></i> 系统管理</el-breadcrumb-item>
                <el-breadcrumb-item>用户管理</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="handle-box">
            <el-button type="primary" :disabled="disable" icon="search" @click="addUserFormVisible=true">添加用户</el-button>
            <el-input v-model="select_word" placeholder="搜索用户" class="handle-input mr10"></el-input>
            <el-button type="primary" icon="search" @click="search">搜索</el-button>
        </div>
        <el-table :data="users" border stripe style="width: 100%" ref="multipleTable" @selection-change="handleSelectionChange">
            <el-table-column type="selection" width="55"></el-table-column>
            <el-table-column prop="id" label="用户ID" sortable width="150">
            </el-table-column>
            <el-table-column prop="username" label="用户名称">
            </el-table-column>
            <el-table-column prop="email" label="用户邮箱">
            </el-table-column>
            <el-table-column prop="is_superuser" label="是否管理员" :formatter="booleanFormat">
            </el-table-column>
            <el-table-column label="操作" width="180">
                <template scope="scope">
                    <el-button size="small" :disabled="disable"
                            @click="handleEdit(scope.$index, scope.row)">激活用户</el-button>
                    <el-button size="small" type="danger" :disabled="disable"
                            @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
        <div class="pagination">
            <el-pagination
              @current-change="handleCurrentChange"
              :current-page="cur_page"
              :page-sizes="[10]"
              :page-size="100"
              layout="total, sizes, prev, pager, next, jumper"
              :total="total">
            </el-pagination>
        </div>
<!--         <editProject :editProjectFormVisible.sync="editProjectFormVisible" :row=row></editProject> -->
        <addUser :addUserFormVisible.sync="addUserFormVisible"></addUser>
    </div>
</template>

<script>
    import api from '../../api/api.js';
    import addUser from './addUser.vue';

    export default {
        data() {
            return {
                url: `${api.host}/users/`,
                users: [],
                cur_page: 1,
                multipleSelection: [],
                select_cate: "我的项目",
                select_word: '',
                del_list: [],
                editUserFormVisible: false,
                addUserFormVisible: false,
                row: {},
                hide: false,
                disable: true,
                total: 0,
            }
        },
        created(){
            this.initUrl();
            this.getUsers();
            this.isAdmin();
        },
        computed: {

        },
        components: {
            addUser
        },
        methods: {
            initUrl(val){
                this.url = `${api.host}/users/`;
                this.url=this.url + `?page=${this.cur_page}`;

                if (val === "search"){
                    this.url=this.url + `&search=${this.select_word}`;
                }
            },
            booleanFormat(row, column){
                if (row.is_superuser){
                    return "是";
                }else{
                    return "否"
                }
            },
            isAdmin(){
                this.disable=(localStorage.getItem("is_superuser")==='false');
            },
            handleMyProjects(){

            },
            handleCurrentChange(val){
                this.cur_page = val;
                this.initUrl();
                this.getUsers();
            },
            getUsers(){
                let self = this;
                self.$http.get(self.url)
                    .then((response) => {
                        self.users=response.data.results;
                        self.total = response.data.count;
                    })
            },
            search(){
                this.cur_page = 1;
                this.initUrl('search');
                this.getUsers();
            },
            formatter(row, column) {
                return row.address;
            },
            filterTag(value, row) {
                return row.tag === value;
            },
            handleEdit(index, row) {
                alert("开发中。。。");
            },
            handleDelete(index, row) {
                alert("暂不提供删除！");
            },
            delAll(){
                const self = this,
                    length = self.multipleSelection.length;
                let str = '';
                self.del_list = self.del_list.concat(self.multipleSelection);
                for (let i = 0; i < length; i++) {
                    str += self.multipleSelection[i].name + ' ';
                }
                self.$message.error('删除了'+str);
                self.multipleSelection = [];
            },
            handleSelectionChange(val) {
                this.multipleSelection = val;
            }
        }
    }
</script>

<style scoped>
.handle-box{
    margin-bottom: 20px;
}
.handle-select{
    width: 120px;
}
.handle-input{
    width: 300px;
    display: inline-block;
}
</style>