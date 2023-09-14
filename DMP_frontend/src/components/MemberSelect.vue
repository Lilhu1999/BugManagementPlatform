<!--<script>-->
<!--export default {-->
<!--  data() {-->
<!--    return {-->
<!--      member: [{-->
<!--          id: 1,-->
<!--          label: '一级 1',-->
<!--          children: [{-->
<!--            id: 4,-->
<!--            label: '二级 1-1',-->
<!--          }]-->
<!--        }, {-->
<!--          id: 2,-->
<!--          label: '一级 2',-->
<!--          children: [{-->
<!--            id: 5,-->
<!--            label: '二级 2-1'-->
<!--          }, {-->
<!--            id: 6,-->
<!--            label: '二级 2-2'-->
<!--          }]-->
<!--        }, {-->
<!--          id: 3,-->
<!--          label: '一级 3',-->
<!--          children: [{-->
<!--            id: 7,-->
<!--            label: '二级 3-1'-->
<!--          }, {-->
<!--            id: 8,-->
<!--            label: '二级 3-2'-->
<!--          }]-->
<!--        }],-->
<!--      defaultProps: {-->
<!--        children: 'children',-->
<!--        label: 'label',-->
<!--      },-->
<!--      value:[],-->
<!--      selectTree:[],-->
<!--    }-->
<!--  },-->
<!--  methods:{-->

<!--  },-->
<!--}-->
<!--</script>-->

<!--<template>-->
<!--<div>-->
<!--  <el-select v-model="value" placeholder="请选择项目成员" style="width: 100%">-->
<!--    <el-option class="option_style">-->
<!--      <el-tree-->
<!--        :data="member"-->
<!--        show-checkbox-->
<!--        node-key="id"-->
<!--        ref="tree"-->
<!--        :props="defaultProps">-->
<!--      </el-tree>-->
<!--    </el-option>-->
<!--  </el-select>-->
<!--</div>-->
<!--</template>-->

<!--<style scoped>-->
<!--.option_style {-->
<!--  min-height: 200px;-->
<!--	padding: 0 !important;-->
<!--	margin: 0;-->
<!--	overflow: auto;-->
<!--	cursor: default !important-->
<!--}-->
<!--</style>-->
