<template>
  <div class="home">
    <el-card>
      <template #header>
        <h2>📊 数据总览</h2>
      </template>
      
      <el-row :gutter="20">
        <el-col :span="6">
          <el-statistic title="总书签数" :value="stats.total" />
        </el-col>
        <el-col :span="6">
          <el-statistic title="独立域名" :value="stats.domains" />
        </el-col>
        <el-col :span="6">
          <el-statistic title="技能数量" :value="stats.skills" />
        </el-col>
        <el-col :span="6">
          <el-statistic title="学习月数" :value="stats.months" />
        </el-col>
      </el-row>
    </el-card>

    <el-row :gutter="20" style="margin-top: 20px;">
      <el-col :span="12">
        <el-card>
          <template #header>
            <h3>🌐 热门域名 TOP 5</h3>
          </template>
          <el-table :data="topDomains" style="width: 100%">
            <el-table-column prop="domain" label="域名" />
            <el-table-column prop="count" label="数量" width="100" />
          </el-table>
        </el-card>
      </el-col>
      
      <el-col :span="12">
        <el-card>
          <template #header>
            <h3>📚 技术领域分布</h3>
          </template>
          <div ref="chartRef" style="height: 300px;"></div>
        </el-card>
      </el-col>
    </el-row>

    <el-card style="margin-top: 20px;">
      <template #header>
        <h3>🎯 核心技能 TOP 10</h3>
      </template>
      <el-table :data="topSkills" style="width: 100%">
        <el-table-column prop="skill" label="技能" />
        <el-table-column prop="category" label="类别" width="120" />
        <el-table-column prop="count" label="次数" width="100" />
      </el-table>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import * as echarts from 'echarts'

const stats = ref({
  total: 328,
  domains: 108,
  skills: 45,
  months: 35,
})

const topDomains = ref([
  { domain: 'blog.csdn.net', count: 73 },
  { domain: 'zhuanlan.zhihu.com', count: 34 },
  { domain: 'cnblogs.com', count: 24 },
  { domain: 'cloud.tencent.com', count: 17 },
  { domain: 'github.com', count: 15 },
])

const topSkills = ref([
  { skill: 'Flink', category: '大数据', count: 41 },
  { skill: 'Hudi', category: '大数据', count: 35 },
  { skill: 'OpenStack', category: '云计算', count: 32 },
  { skill: 'CVM', category: '云计算', count: 18 },
  { skill: 'Java', category: '编程语言', count: 10 },
  { skill: 'Go', category: '编程语言', count: 9 },
  { skill: 'Python', category: '编程语言', count: 8 },
  { skill: 'Transformer', category: '深度学习', count: 9 },
  { skill: 'PyTorch', category: '深度学习', count: 6 },
  { skill: '昇腾', category: 'AI 芯片', count: 5 },
])

const chartRef = ref<HTMLElement>()

onMounted(() => {
  if (chartRef.value) {
    const chart = echarts.init(chartRef.value)
    chart.setOption({
      tooltip: { trigger: 'item' },
      series: [{
        type: 'pie',
        radius: '50%',
        data: [
          { value: 100, name: '大数据' },
          { value: 56, name: '云计算' },
          { value: 27, name: 'AI/大模型' },
          { value: 21, name: '编程语言' },
          { value: 13, name: 'AI 芯片' },
        ],
      }],
    })
  }
})
</script>
