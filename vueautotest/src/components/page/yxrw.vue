<template>
    <div class="table">
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-menu"></i> 项目管理</el-breadcrumb-item>
                <el-breadcrumb-item>项目管理</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="handle-box">
            <el-button type="primary" icon="search" @click="addProjectFormVisible=true">添加项目</el-button>
            <el-select v-model="select_cate" placeholder="筛选项目" class="handle-select mr10" @change="handleMyProjects">
                <el-option key="1" :disabled="disable" label="所有项目" value="所有项目"></el-option>
                <el-option key="2" label="我的项目" value="我的项目"></el-option>
            </el-select>
            <el-input v-model="select_word" placeholder="搜索所有项目" class="handle-input mr10"></el-input>
            <el-button type="primary" icon="search" @click="search">搜索</el-button>
        </div>
        <el-table :data="projects" border stripe style="width: 100%" ref="multipleTable" @selection-change="handleSelectionChange">
            <el-table-column type="selection" width="55"></el-table-column>
            <el-table-column prop="id" label="项目ID" sortable width="150">
            </el-table-column>
            <el-table-column prop="project_name" label="项目名称" fit>
            </el-table-column>
            <el-table-column  label="用户" v-if="hide">
                <template slot-scope="scope" >
                    {{ scope.row.user }}
                </template>
            </el-table-column>

            <el-table-column label="操作" width="180">
                <template scope="scope">
                    <el-button size="small"
                            @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                    <el-button size="small" type="danger"
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
        <editProject :editProjectFormVisible.sync="editProjectFormVisible" :row=row></editProject>
        <addProject :addProjectFormVisible.sync="addProjectFormVisible"></addProject>
    </div>
</template>

<script>
    import api from '../../api/api.js';
    import editProject from './editProject.vue';
    import addProject from './addProject.vue';

    export default {
        data() {
            return {
                url: `${api.host}/projects/`,
                projects: [],
                cur_page: 1,
                multipleSelection: [],
                select_cate: "我的项目",
                select_word: '',
                del_list: [],
                editProjectFormVisible: false,
                addProjectFormVisible: false,
                row: {},
                hide: false,
                disable: true,
                total: 0,
            }
        },
        created(){
            this.initUrl();
            this.getProjects();
            this.isAdmin();
        },
        computed: {

        },
        components: {
            editProject,
            addProject
        },
        methods: {
            initUrl(val){
                this.url = `${api.host}/projects/`;
                this.url=this.url + `?page=${this.cur_page}`;
                if (this.select_cate === "我的项目"){
                    let userid = localStorage.getItem("ms_userid");
                    this.url=this.url + `&user=${userid}`;
                }

                if (val === "search"){
                    this.url=this.url + `&search=${this.select_word}`;
                }
            },
            isAdmin(){
                this.disable=(localStorage.getItem("is_superuser")==='false');
            },
            addProject(){
                self.$http.post(`${api.host}/projects/`, this.ruleForm)
                    .then((response) => {

                })
            },
            handleMyProjects(){
                this.initUrl();
                this.getProjects();
            },
            handleCurrentChange(val){
                this.cur_page = val;
                this.initUrl();
                this.getProjects();
            },
            getProjects(){
                let self = this;
                self.$http.get(self.url)
                    .then((response) => {
                        self.projects=response.data.results;
                        self.total = response.data.count;
                    })
            },
            search(){
                this.cur_page = 1;
                this.initUrl('search');
                this.getProjects();
            },
            formatter(row, column) {
                return row.address;
            },
            filterTag(value, row) {
                return row.tag === value;
            },
            handleEdit(index, row) {
                this.row = row;
                this.editProjectFormVisible = true;
            },
            handleDelete(index, row) {
                this.$http.delete(`${api.host}/projects/${row.id}`)
                .then((response) => {
                    this.getProjects();
                })
                this.$message.error('删除第'+(index+1)+'行');
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