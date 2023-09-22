<script>
export default {
  data() {
    return {
      treeData:[],
      defaultProps: {
          children: 'children',
          label: 'name',
          pid:'id'
        },
      selectTree:[],
      value:[],
      id:[],
    }
  },
  mounted() {
    this.getTreeData()
  },
  methods: {
    handleNodeClick(data) {
      console.log(data);
    },
    getNodeData(data, hasPick) {
      if (hasPick) {
        this.value = data['name']
        this.id = data['id']
        this.$emit('getPid',this.id)
      }else {
        this.value = []
        this.id = []
      }
    },
    getTreeData() {
      this.$axios.get('api/getTree/',{
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.treeData = res['list']
        }else {
          console.log(res['respMsg'])
        }
      })
    },
  },
}
</script>

<template>
  <div>
    <el-select v-model="value" size="small">
      <el-option :value="selectTree" class="opsty">
        <el-tree
          :data="treeData"
          :props="defaultProps"
          accordion
          show-checkbox
          @node-click="handleNodeClick"
          @check-change="getNodeData"
        >
        </el-tree>
      </el-option>
    </el-select>
  </div>
</template>

<style scoped>
.opsty {
  width: 100%;
  min-height: 200px;
  padding: 0 !important;
  margin: 0 ;
  overflow: auto;
}
</style>
