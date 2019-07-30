function getAllMonthlyData(val) {
    let data = [];
    let years = [2013, 2014, 2015, 2016, 2017, 2018, 2019];
    // 首先获取有哪些年份
    for (let y of years) data = data.concat(getYearData(val, y))
    for (let d in data) data[d][0] = d;

    // 计算最大AQI
    let max_aqi = 300;
    // for (let e of data) {
    //     if (parseInt(e[1]) > max_aqi) {
    //         max_aqi = parseInt(e[1]);
    //     }
    // }

    console.log(max_aqi);
    // 将无数据的月份数据替换为最大AQI
    for (let i = 0; i < data.length; i++) {
        if (data[i][1] == null) {
            data[i][1] = max_aqi;
        }
    }


    return data;
}