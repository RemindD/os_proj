# Draw figure for experiment result
import matplotlib.pyplot as plt

if __name__ == "__main__":
    arraySize = [12]
    for i in range(19):
        arraySize.append(arraySize[-1]+1)
    memoryAccessTime0 = [9.190000, 8.570000, 8.590000, 8.330000, 9.020000, 10.710000, 10.440000, 10.670000, 9.620000,
                         12.550000, 12.010000, 12.460000, 15.080000, 16.800000, 14.010000, 20.060000, 15.180000,
                         14.660000, 14.340000, 15.220000]
    memoryAccessTime1 = [10.990000, 11.240000, 11.310000, 11.130000, 12.220000, 14.400000, 12.760000, 17.120000, 
                         12.140000, 16.190000, 14.280000, 15.300000, 14.220000, 14.440000, 14.100000, 22.100000,
                         17.260000, 24.580000, 16.460000, 19.040000]
    memoryAccessTime2 = [11.370000, 10.890000, 10.100000, 10.850000, 16.570000, 18.980000, 23.940000, 20.110000, 
                         22.180000, 22.300000, 22.080000, 21.330000, 21.310000, 21.780000, 22.480000, 39.490000,
                         30.810000, 40.800000, 39.650000, 33.390000]
    memoryAccessTime3 = [11.400000, 10.500000, 10.750000, 11.310000, 16.400000, 18.360000, 23.190000, 76.750000, 
                         114.930000, 129.610000, 132.890000, 168.250000, 151.690000, 161.390000, 151.010000, 167.250000,
                         170.530000, 179.140000, 177.570000, 195.780000]
    memoryAccessTime4 = [11.350000, 10.770000, 10.680000, 11.070000, 16.960000, 16.820000, 24.460000, 93.590000, 
                         140.240000, 158.130000, 164.770000, 213.250000, 216.450000, 270.090000, 239.920000, 259.660000,
                         198.700000, 212.400000, 212.410000, 160.950000]
    memoryAccessTime5 = [11.340000, 11.160000, 10.460000, 11.090000, 18.370000, 19.000000, 20.970000, 115.740000,
                         201.520000, 183.500000, 234.570000, 267.670000, 275.690000, 342.730000, 273.790000, 293.740000,
                         256.240000, 294.840000, 271.310000, 307.930000]
    plt.figure()
    plt.plot(arraySize[:15], memoryAccessTime0[:15], label="4B")
    plt.plot(arraySize[:15], memoryAccessTime1[:15], label="16B")
    plt.plot(arraySize[:15], memoryAccessTime2[:15], label='64B')
    plt.plot(arraySize[:15], memoryAccessTime3[:15], label="256B")
    plt.plot(arraySize[:15], memoryAccessTime4[:15], label="1M")
    plt.plot(arraySize[:15], memoryAccessTime5[:15], label="4M")
    plt.legend()
    plt.xlabel("log2(array size)")
    plt.ylabel("latency in clock cycle")
    plt.show()