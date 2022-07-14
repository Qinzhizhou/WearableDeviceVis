var chartDom = document.getElementById('chart1');
var myChart = echarts.init(chartDom);
var option;

option = {
  xAxis: {
    type: 'category',
    data: {{ timelines|safe }},
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      data: {{ heartrates|safe }},
      type: 'line'
    }
  ]
};

option && myChart.setOption(option);