<template>
    <div class="sidebar">
        <el-menu :default-active="onRoutes" class="el-menu-vertical-demo" theme="dark" unique-opened router>
            <template v-for="item in items">
                <template v-if="item.subs">
                    <el-submenu :index="item.index">
                        <template slot="title"><i :class="item.icon"></i>{{ item.title }}</template>
                        <el-menu-item v-for="(subItem,i) in item.subs" :key="i" :index="subItem.index">{{ subItem.title }}
                        </el-menu-item>
                    </el-submenu>
                </template>
                <template v-else>
                    <el-menu-item :index="item.index">
                        <i :class="item.icon"></i>{{ item.title }}
                    </el-menu-item>
                </template>
            </template>
        </el-menu>
    </div>
</template>

<script>
    import api from '../../api/api.js';
    export default {
        data() {
            return {
                items: [
                    {
                        icon: 'el-icon-setting',
                        index: 'readme',
                        title: '首页'
                    },
                    {
                        icon: 'el-icon-setting',
                        index: '2',
                        title: '系统管理',
                        subs: [
                            {
                                index: 'yhgl',
                                title: '用户管理'
                            },
                            {
                                index: 'xmgl',
                                title: '项目管理'
                            }
                        ]
                    },
                    {
                        icon: 'el-icon-menu',
                        index: '3',
                        title: '任务管理',
                        subs: [
                            {
                                index: 'csrw',
                                title: '测试任务'
                            },
                            {
                                index: 'csjrw',
                                title: '测试集任务'
                            },
                            {
                                index: 'yxrw',
                                title: '运行任务'
                            }
                        ]
                    },
                    {
                        icon: 'el-icon-menu',
                        index: '4',
                        title: '监控',
                        subs: [
                            {
                                index: 'jenkins',
                                title: 'Jenkins监控'
                            },
                            {
                                index: 'sonarqube',
                                title: 'SonarQube监控'
                            },
                            {
                                index: 'harbor',
                                title: 'Harbor监控'
                            }
                        ]
                    },
                    {
                        icon: 'el-icon-menu',
                        index: '5',
                        title: '表格',
                        subs: [
                            {
                                index: 'basetable',
                                title: '基础表格'
                            },
                            {
                                index: 'vuetable',
                                title: 'Vue表格组件'
                            }
                        ]
                    },
                    {
                        icon: 'el-icon-date',
                        index: '6',
                        title: '表单',
                        subs: [
                            {
                                index: 'baseform',
                                title: '基本表单'
                            },
                            {
                                index: 'vueeditor',
                                title: '编辑器'
                            },
                            {
                                index: 'markdown',
                                title: 'markdown'
                            },
                            {
                                index: 'upload',
                                title: '文件上传'
                            }
                        ]
                    },
                    {
                        icon: 'el-icon-star-on',
                        index: 'basecharts',
                        title: '图表'
                    },
                    {
                        icon: 'el-icon-upload2',
                        index: 'drag',
                        title: '拖拽'
                    }
                ]
            }
        },
        computed:{
            onRoutes(){
                return this.$route.path.replace('/','');
            }
        },
        created(){},
        methods: {
            getMenus(){
                let self=this;
                self.$http.get(`${api.host}/menus/`)
                .then((response) => {
                    console.log(response);
                })
            }
        }
    }
</script>

<style scoped>
    .sidebar{
        display: block;
        position: absolute;
        width: 250px;
        left: 0;
        top: 70px;
        bottom:0;
        background: #2E363F;
    }
    .sidebar > ul {
        height:100%;
    }
</style>
