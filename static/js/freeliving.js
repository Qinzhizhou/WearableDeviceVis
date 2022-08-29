var chartDom = document.getElementById('chart1');
var myChart = echarts.init(chartDom);
var option;
window.onresize = function() {myChart.resize();};

option = {title : {text: 'The Visualization of Freeliving Experiment', x: 'left'},

  color: ['#FF0087', '#0d0d0d', '#00cc99', '#e69419',  '#33ffcc'],
  dataZoom: [
{
  type: 'inside',
  start: 0,
  end: 100
}, {
  start: 0,
  end: 100
}
],

  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'cross',
      label: {
        backgroundColor: '#6a7985'
      }
    }
  },
  legend: {
    data: ['A', 'B', 'C', 'D', 'E'],
    x: 'right',
    padding:[10,35,0,0]

  },
  toolbox: {
    feature: {
      saveAsImage: {}
    }
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  xAxis: [
    {
      type: 'category',
      boundaryGap: false,
      data: timelines
    }
  ],
  yAxis: [
    {
      type: 'value'
    }
  ],
  series: [
    {
      name: 'A',
      type: 'line',
      smooth: true,

      lineStyle: {
        width: 0
      },
      showSymbol: false,
      areaStyle: {
        opacity: 0.8,
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          {
            offset: 0,
            color: 'rgb(255, 0, 135)'
          },
          {
            offset: 0.6,
            color: 'rgb(255, 0, 135)'
          }
        ])
      },
      emphasis: {
        focus: 'series'
      },
      data: va
    },
    {
      name: 'B',
      type: 'line',

      smooth: true,
      lineStyle: {
        width: 0
      },
      showSymbol: false,
      areaStyle: {
        opacity: 0.8,
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          {
            offset: 0,
            color: '#666666'
          },
          {
            offset: 0.5,
            color: '#0d0d0d'
          }
        ])
      },
      emphasis: {
        focus: 'series'
      },
      data: vb
    },
    {
      name: 'C',
      type: 'line',

      smooth: true,
      lineStyle: {
        width: 0
      },
      showSymbol: false,
      areaStyle: {
        opacity: 0.8,
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          {
            offset: 0,
            color: '#00cc99'
          },
          {
            offset: 0.5,
            color: '#00cc99'
          }
        ])
      },
      emphasis: {
        focus: 'series'
      },
      data: vc
    },
    {
      name: 'D',
      type: 'line',

      smooth: true,
      lineStyle: {
        width: 0
      },
      showSymbol: false,
      areaStyle: {
        opacity: 0.8,
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          {
            offset: 0.5,
            color: '#e69419'
          },
          {
            offset: 1,
            color: '#e69419'
          }
        ])
      },
      emphasis: {
        focus: 'series'
      },
      data: vd
    },
    {
      name: 'E',
      type: 'line',

      smooth: true,
      lineStyle: {
        width: 0
      },
      showSymbol: false,
      label: {
        show: true,
        position: 'top'
      },
      areaStyle: {
        opacity: 0.8,
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          {
            offset: 0,
            color: '#33ffcc'
          },
          {
            offset: 1,
            color: '#33ffcc'
          }
        ])
      },
      emphasis: {
        focus: 'series'
      },
      data: ve
    }
  ]
};

option && myChart.setOption(option);



var chartDom2 = document.getElementById('chart2');
var myChart2 = echarts.init(chartDom2);
var option2;


// prettier-ignore
var days = [
    'A', 'B', 'C',
    'D', 'E'
];

var data = [];
for (let i = 0; i < hours.length; i++) {
  data.push([0,i,va[i], na[i]]);
  data.push([1,i,vb[i], nb[i]]);
  data.push([2,i,vc[i], nc[i]]);
  data.push([3,i,vd[i], nd[i]]);
  data.push([4,i,ve[i], ne[i]])
}


const title = [];
var singleAxis = [];
var series = [];

days.forEach(function (day, idx) {
  title.push({
    textBaseline: 'middle',
    top: ((idx + 0.5) * 100) / 7 + '%',
    text: day
  });

  singleAxis.push({
    left: 150,
    type: 'category',
    boundaryGap: false,
    data: hours,
    top: (idx * 120) / 7 + 5 + '%',
    height: 120 / 7 - 10 + '%',
  });
  series.push({
    singleAxisIndex: idx,
    coordinateSystem: 'singleAxis',
    type: 'scatter',
    data: [],
    symbolSize: function (dataItem) {
      return dataItem[1] * 30;
        // return dataItem[1].map(normalization)
    }
  });
});
data.forEach(function (dataItem) {

  series[dataItem[0]].data.push([dataItem[1], dataItem[3]]); // normalize
});


option2 = {
  tooltip: {
      position: 'top',
      trigger: 'axis',
  },
    toolbox: {
    feature: {
        dataZoom: {yAxisIndex: 'none'
        }
    },
      restore: {},
      saveAsImage: {}
    },
  title: title,
  singleAxis: singleAxis,
  series: series,
};

option2 && myChart2.setOption(option2);

