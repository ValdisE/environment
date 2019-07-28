/**
 * 获取某年的数据，只包含月份的AQI（月平均）
 * @param {Array} val 
 * @param {int} year 
 */
function getYearData(val, year) {
    let data = [];
    let monthData = new Array(12);
    for (let i = 0; i < monthData.length; i++) {
        monthData[i] = {
            totalAQI: 0,
            dayNum: 0
        }
    }
    for (let day of val) {
        let day_arr = day.date.split('-');
        let yy = day_arr[0],
            mm = day_arr[1],
            dd = day_arr[2];
        if (yy == year) {
            monthData[parseInt(mm) - 1].totalAQI += parseInt(day.score);
            monthData[parseInt(mm) - 1].dayNum++;
        }
    }
    for (let i = 0; i < monthData.length; i++) {
        if (monthData[i].dayNum == 0) {
            data.push([i, null]);
        } else {
            data.push([i, (monthData[i].totalAQI / monthData[i].dayNum).toFixed(1)]);
        }
    }
    let max_aqi = Number.MIN_VALUE;
    for (let e of data) {
        if (parseInt(e[1]) > max_aqi) {
            max_aqi = parseInt(e[1]);
        }
    }
    for (let i = 0; i < data.length; i++) {
        if (data[i][1] == null) {
            data[i][1] = max_aqi;
        }
    }
    console.log(data);
    return data;
}