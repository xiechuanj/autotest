<template>
    <div class="table">
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-menu"></i> 任务管理</el-breadcrumb-item>
                <el-breadcrumb-item>测试任务</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="handle-box">
            <el-button type="primary" icon="search" @click="addTaskFormVisible=true">添加任务</el-button>
            <el-select v-model="select_cate" placeholder="筛选项目" class="handle-select mr10" @change="handleSelectProjectsOption">
                <el-option key="1" :disabled="disable" label="所有项目" value="所有项目"></el-option>
                <el-option key="2" label="我的项目" value="我的项目"></el-option>
            </el-select>
            <el-select v-model='project' placeholder="选择项目" class="handle-select mr10" @change="handleProjects()" >
                <el-option
                 v-for="project in projects"
                 :key="project.id"
                 :disabled="disable"
                 :label="project.project_name"
                 :value="project.project_name">
                 </el-option>
            </el-select>
            <el-input v-model="select_word" placeholder="搜索所有任务" class="handle-input mr10"></el-input>
            <el-button type="primary" icon="search" @click="search">搜索</el-button>
        </div>
        <el-table :data="tasks" border stripe style="width: 100%" ref="multipleTable" @selection-change="handleSelectionChange">
            <el-table-column type="selection" width="55"></el-table-column>
            <el-table-column prop="id" label="任务ID" sortable width="150">
            </el-table-column>
            <el-table-column prop="task_name" label="任务名称" fit>
            </el-table-column>
            <el-table-column  label="所属项目" v-if="hide">
                <template slot-scope="scope" >
                    {{ scope.row.projects }}
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
        <editTask :editTaskFormVisible.sync="editTaskFormVisible" :row=row></editTask>
        <addTask :addTaskFormVisible.sync="addTaskFormVisible" :projectId.sync="projectId"></addTask>
    </div>
</template>

<script>
    import api from '../../api/api.js';
    import editTask from './editTask.vue';
    import addTask from './addTask.vue';


    export default {
        data() {
            return {
                url: `${api.host}/projects/`,
                projects: [],
                project: '',
                projectId: 0,
                cur_page: 1,
                multipleSelection: [],
                select_cate: "我的项目",
                select_word: '',
                del_list: [],
                editTaskFormVisible: false,
                addTaskFormVisible: false,
                row: {},
                hide: false,
                disable: true,
                total: 0,
                tasks: [],

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
            editTask,
            addTask
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
            getProjectIdFromName(name){
                let self=this;
                self.url = `${api.host}/projects/?project_name=${self.project}`
                self.$http.get(self.url)
                    .then((response) => {
                        if (response.data.count>0){
                            self.projectId = response.data.results[0].id;
                        }
                    })
            },
            handleProjects(){
                let self=this;
                self.getProjectIdFromName(this.project);
            },
            handleTasks(){
                let self=this;
                self.url = `${api.host}/tasks/?projects=${self.projectId}&search=${self.select_word}`;
                self.$http.get(self.url)
                .then((response) => {
                    self.tasks = response.data.results;
                    self.total = response.data.count;
                })
            },
            handleSelectProjectsOption(){
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
                this.handleTasks();
            },
            formatter(row, column) {
                return row.address;
            },
            filterTag(value, row) {
                return row.tag === value;
            },
            handleEdit(index, row) {
                this.row = row;
                this.editTaskFormVisible = true;
            },
            handleDelete(index, row) {
                this.$http.delete(`${api.host}/tasks/${row.id}`)
                .then((response) => {
                    this.handleTasks();
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