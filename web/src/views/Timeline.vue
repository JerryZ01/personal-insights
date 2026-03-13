<template>
  <div class="timeline">
    <el-card>
      <template #header>
        <h2>📅 学习轨迹</h2>
      </template>
      
      <el-timeline>
        <el-timeline-item 
          v-for="(phase, index) in phases" 
          :key="index" 
          :timestamp="phase.period"
          placement="top"
          :color="getPhaseColor(phase.category)"
        >
          <el-card>
            <h3>{{ phase.category }}</h3>
            <p>收藏数量：{{ phase.count }}篇</p>
          </el-card>
        </el-timeline-item>
      </el-timeline>
    </el-card>

    <el-card style="margin-top: 20px;">
      <template #header>
        <h3>📊 月度趋势</h3>
      </template>
      <div ref="chartRef" style="height: 400px;"></div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import * as echarts from 'echarts'

const phases = ref([
  { period: '2022-03 - 2022-06', category: '大数据', count: 74 },
  { period: '2022-06 - 2022-09', category: '云计算', count: 44 },
  { period: '2022-09 - 2022-10', category: '编程语言', count: 10 },
  { period: '2022-10 - 2023-05', category: '大数据', count: 69 },
  { period: '2023-07 - 2024-02', category: '云计算', count: 64 },
  { period: '2024-02 - 2025-02', category: 'AI/大模型', count: 51 },
])

const getPhaseColor = (category: string): string => {
  const colors: Record<string, string> = {
    '大数据': '#E6A23C',
    '云计算': '#409EFF',
    '编程语言': '#67C23A',
    'AI/大模型': '#F56C6C',
  }
  return colors[category] || '#909399'
}

const chartRef = ref<HTMLElement>()

onMounted(() => {
  if (chartRef.value) {
    const chart = echarts.init(chartRef.value)
    chart.setOption({
      tooltip: { trigger: 'axis' },
      xAxis: {
        type: 'category',
        data: ['2023-09', '2023-10', '2023-11', '2023-12', '2024-01', '2024-02', '2024-03', '2024-04'],
      },
      yAxis: {
        type: 'value',
        name: '收藏数',
      },
      series: [{
        data: [2, 4, 4, 6, 10, 5, 24, 22],
        type: 'bar',
        showBackground: true,
        itemStyle: { color: '#409EFF' },
      }],
    })
  }
})
</script>
