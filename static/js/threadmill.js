 if (condition == 1) {
        console.log("The type of id is heart rate")
        var time = t1
        const button = document.createElement('button')
      // Set the button text to 'Can you click me?'
      button.innerText = 'Change the days in chart2'
      button.id = 'mainButton'
      // Attach the "click" event to your button
      button.addEventListener('click', () => {
        // When there is a "click"
        // it shows an alert in the browser
          if (time == t1 ){
              time = t2;chart2()}
          else {time = t1;chart2()}
        }
      )
      document.body.appendChild(button)
        chart1()
        chart2()}
    else if (condition == 2){
         console.log("The type of id others");
         chart3();
         chart4();
    }


function chart1()
{ var chartDom = document.getElementById('chart1');
        var myChart = echarts.init(chartDom);
        var option = {
            color: ['#FF0087', '#0d0d0d', '#00cc99', '#e69419'],
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                  type: 'cross',
                  label: {
                    backgroundColor: '#6a7985'
                  }
                }
              },

              toolbox: {
                feature: {
                  saveAsImage: {}
                }
              },
              grid: [
                { left: '38px', right: '33px', top: '20%', height: '25%' },
                { left: '38px', right: '33px', top: '53%', height: '25%' }
              ],

              axisPointer: {
                   link: {xAxisIndex: 'all'}
               },
              legend: {
                data: ['GT', 'Fitbit Charge HR', 'Fitbit Charge 2', 'Fitbit Surge'],
              },
              xAxis: [
                {
                  gridIndex: 0,
                  boundaryGap: false,
                  type: 'category',
                  data: t1
                },
                {
                  gridIndex: 1,
                  boundaryGap: false,
                  type: 'category',
                  data: t2
                }
              ],


            yAxis: [{ gridIndex: 0, type: 'value' },{  gridIndex: 1,type: 'value' }],
              series: [
                        {
                          name: 'GT',
                          type: 'line',
                          smooth: true, xAxisIndex: 0, yAxisIndex: 0,


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
                          data: va.slice(0, t1.length)
                        },
                         {
                          name: 'GT',
                          type: 'line',
                          smooth: true, xAxisIndex: 1, yAxisIndex: 1, // set the index
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
                          data: va.slice(t1.length, t1.length + t2.length)
                        },

                  {
                          name: 'Fitbit Charge HR',
                          type: 'line',
                          smooth: true, xAxisIndex: 0, yAxisIndex: 0,


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
                                offset: 0.3,
                                color: '#0d0d0d'
                              }
                            ])
                          },
                          emphasis: {
                            focus: 'series'
                          },
                          data: vb.slice(0, t1.length)
                        },
                         {
                          name: 'Fitbit Charge HR',
                          type: 'line',
                          smooth: true, xAxisIndex: 1, yAxisIndex: 1, // set the index
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
                                        offset: 0.3,
                                        color: '#0d0d0d'
                                      }
                            ])
                          },
                          emphasis: {
                            focus: 'series'
                          },
                          data: vb.slice(t1.length, t1.length + t2.length)
                        },

                  {
                          name: 'Fitbit Charge 2',
                          type: 'line',
                          smooth: true, xAxisIndex: 0, yAxisIndex: 0,


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
                            offset: 0.3,
                            color: '#00cc99'
                          }
                            ])
                          },
                          emphasis: {
                            focus: 'series'
                          },
                          data: vc.slice(0, t1.length)
                        },
                         {
                          name: 'Fitbit Charge 2',
                          type: 'line',
                          smooth: true, xAxisIndex: 1, yAxisIndex: 1, // set the index
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
                                offset: 0.3,
                                color: '#00cc99'
                              }
                            ])
                          },
                          emphasis: {
                            focus: 'series'
                          },
                          data: vc.slice(t1.length, t1.length + t2.length)
                        },

                     {
                          name: 'Fitbit Surge',
                          type: 'line',
                          smooth: true, xAxisIndex: 0, yAxisIndex: 0,


                          lineStyle: {
                            width: 0
                          },
                          showSymbol: false,
                          areaStyle: {
                            opacity: 0.8,
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                          {
                                    offset: 0,
                                    color: '#e69419'
                                  },
                                  {
                                    offset: 0.3,
                                    color: '#e69419'
                                  }
                            ])
                          },
                          emphasis: {
                            focus: 'series'
                          },
                          data: vc.slice(0, t1.length)
                        },
                         {
                          name: 'Fitbit Surge',
                          type: 'line',
                          smooth: true, xAxisIndex: 1, yAxisIndex: 1, // set the index
                          lineStyle: {
                            width: 0
                          },
                          showSymbol: false,
                          areaStyle: {
                            opacity: 0.8,
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                               {
                                offset: 0,
                                color: '#e69419'
                              },
                              {
                                offset: 0.3,
                                color: '#e69419'
                              }
                            ])
                          },
                          emphasis: {
                            focus: 'series'
                          },
                          data: vc.slice(t1.length, t1.length + t2.length)
                        },
              ]
            };
            option && myChart.setOption(option);
}


function chart2() {
        var chartDom2 = document.getElementById('chart2');
        var myChart2 = echarts.init(chartDom2);
        var option2;
        var data = [];
        var data2 = [];


for (let i = 0; i < time.length; i++) {
  data.push([0,i,va[i], na[i]]);
  data.push([1,i,vb[i], nb[i]]);
  data.push([2,i,vc[i], nc[i]]);
  data.push([3,i,vd[i], nd[i]]);
}

const title = [];
var singleAxis = [];
var series = [];

chargers.forEach(function (chargers, idx) {
  title.push({
    textBaseline: 'middle',
    top: ((idx + 0.5) * 100) / 7 + '%',
    text: chargers
  });

  singleAxis.push({
    left: 150,
    type: 'category',
    boundaryGap: false,
    data: time,
    top: (idx * 120) / 7 + 5 + '%',
    height: 120 / 7 - 10 + '%',
  });



  series.push({
    singleAxisIndex: idx,
    coordinateSystem: 'singleAxis',
    type: 'scatter',
    data: [],
    symbolSize: function (dataItem) {
      return dataItem[1] * 31;
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
}



function chart3() {var chartDom = document.getElementById('chart1');
            var myChart = echarts.init(chartDom);
            var option;
            option = {
                color: ['#FF0087', '#0d0d0d', '#00cc99', '#e69419'],
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
                data:  ['GT', 'Fitbit Charge HR', 'Fitbit Charge 2', 'Fitbit Surge']
              },
              toolbox: {
                feature: {
                  saveAsImage: {}
                }
              },
              grid: {
                left: '3%',
                right: '4%',
                bottom: '10%',
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
                  name: 'GT',
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
                  name: 'Fitbit Charge HR',
                  type: 'line',
                  smooth: true,
                  lineStyle: {
                    width: 0
                  },
                  showSymbol: false,
                  areaStyle: {
                    opacity: 0.3,
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
                  name:  'Fitbit Charge 2',
                  type: 'line',

                  smooth: true,
                  lineStyle: {
                    width: 0
                  },
                  showSymbol: false,
                  areaStyle: {
                    opacity: 0.3,
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
                  name: 'Fitbit Surge',
                  type: 'line',

                  smooth: true,
                  lineStyle: {
                    width: 0
                  },
                  showSymbol: false,
                  areaStyle: {
                    opacity: 0.2,
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
                  data:  vd
                }
              ]
            };

option && myChart.setOption(option)};

function chart4(){
    var chartDom2 = document.getElementById('chart2');
    var myChart2 = echarts.init(chartDom2);
    var option2;
var data = [];
for (let i = 0; i < hours.length; i++) {
  data.push([0,i,va[i], na[i]]);
  data.push([1,i,vb[i], nb[i]]);
  data.push([2,i,vc[i], nc[i]]);
  data.push([3,i,vd[i], nd[i]]);

}


const title = [];
var singleAxis = [];
var series = [];

chargers.forEach(function (chargers, idx) {
  title.push({
    textBaseline: 'middle',
    top: ((idx + 0.5) * 100) / 7 + '%',
    text: chargers
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
      return dataItem[1] * 31;
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
    }