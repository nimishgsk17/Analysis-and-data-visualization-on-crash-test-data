var p1 = {
    type: 'parcoords',
    line: {
        color: [5, 4, 3, 2, 1],
        colourscale: [[5, '#ff0000'], [1, '#ff00ff']]
    },

    dimensions: [{
        // constraintrange: [1, 1.8],
        range: [1, 5],
        label: 'Light Conditions',
        values: [5, 4, 3, 2, 1],
        tickvals: [5, 4, 3, 2, 1],
        ticktext: ['Daytime', 'Dawn', 'Dusk', 'Dark (Lights on)', 'Dark (lights off)']
    }, {
        range: [0, 80000],
        label: 'Passenger Car (Count in accidents)',
        values: [75571, 2143, 2762, 27985, 3309]
    }, {
        range: [0, 12000],
        label: 'Sports utility (Count in accidents)',
        values: [10957, 306, 334, 3067, 388],
    }, {
        range: [0, 5000],
        label: 'Pickup truck (Count in accidents)',
        values: [4584, 181, 148, 1262, 219],
    }, {
        range: [0, 5000],
        label: 'Van (Count in accidents)',
        values: [3689, 95, 78, 735, 102]
    }, {
        range: [0, 3000],
        label: 'Transit Bus (Count in accidents)',
        values: [2646, 75, 68, 637, 32]
    }, {
        range: [0, 3000],
        label: 'School Bus (Count in accidents)',
        values: [2600, 78, 32, 64, 8]
    }, {
        range: [0, 1500],
        label: 'Police (Count in accidents)',
        values: [1042, 48, 36, 646, 181]
    }]
};

var p2 = {
    type: 'parcoords',
    line: {
        color: [8, 7, 6, 5, 4, 3, 2, 1],
        colourscale: [[8, '#ff0000'], [1, '#0000ff']]
    },

    dimensions: [{
        // constraintrange: [1, 1.8],
        range: [1, 8],
        label: 'Movement Before collision',
        values: [8, 7, 6, 5, 4, 3, 2, 1],
        tickvals: [8, 7, 6, 5, 4, 3, 2, 1],
        ticktext: ['Constant speed', 'Slowing/Stopping', 'Stopped in traffic', 'Left turn', 'Accelerating', 'Right Turn', 'Parked', 'Parking']
    }, {
        range: [0, 50000],
        label: 'Passenger car (Count in accidents)',
        values: [45293, 16365, 11809, 11289, 6547, 3231, 1464, 1151]
    }, {
        range: [0, 6000],
        label: 'Sports utility (Count in accidents)',
        values: [5501, 2372, 2027, 1578, 720, 441, 146, 181],
    }, {
        range: [0, 3000],
        label: 'Pickup truck (Count in accidents)',
        values: [2566, 943, 662, 515, 308, 193, 103, 77],
    }, {
        range: [0, 2000],
        label: 'Van (Count in accidents)',
        values: [1708, 723, 548, 462, 217, 137, 112, 56]
    }, {
        range: [0, 1500],
        label: 'Transit bus (Count in accidents)',
        values: [1060, 459, 660, 274, 202, 159, 69, 10]
    }, {
        range: [0, 1000],
        label: 'School bus (Count in accidents)',
        values: [731, 302, 418, 285, 111, 196, 127, 25]
    }, {
        range: [0, 1000],
        label: 'Police (Count in accidents)',
        values: [680, 260, 176, 66, 71, 63, 92, 59]
    }]
};

var p3 = {
    type: 'parcoords',
    line: {
        color: [5, 4, 3, 2, 1],
        colourscale: [[5, '#ff0000'], [1, '#0000ff']]
    },

    dimensions: [{
        // constraintrange: [1, 1.8],
        range: [1, 5],
        label: 'Weather',
        values: [5, 4, 3, 2, 1],
        tickvals: [5, 4, 3, 2, 1],
        ticktext: ["Clear","Cloudy","Foggy","Raining","Snow"]
    }, {
        range: [0, 80000],
        label: 'Passenger Car',
        values: [76512, 10645, 400, 13793, 828]
    }, {
        range: [0, 15000],
        label: 'Sports utility',
        values: [10079, 1818, 79, 1845, 144],
    }, {
        range: [0, 5000],
        label: 'Pickup truck',
        values: [4357, 708, 32, 700, 84],
    }, {
        range: [0, 4000],
        label: 'Van',
        values: [3111, 639, 22, 555, 37]
    }, {
        range: [0, 2500],
        label: 'Transit Bus',
        values: [2319, 430, 9, 361, 44]
    }, {
        range: [0, 2000],
        label: 'School bus',
        values: [1853, 432, 6, 273, 18]
    }, {
        range: [0, 1500],
        label: 'Police',
        values: [1301, 201, 12, 208, 33]
    }]
};

var data1 = [p1]

Plotly.newPlot('PLOT1', data1);

var data2 = [p2]

Plotly.newPlot('PLOT2', data2);

var data3 = [p3]

Plotly.newPlot('PLOT3', data3);