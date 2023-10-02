import statistics
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
class Statistics:
    def mean( data):
        #the mean
         return round(sum(data) / len(data))
        
       
    def median(data):
        #the median 
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
        else:
            return sorted_data[n//2]
    
    def mode(data):
        #the mode
        from collections import Counter
        counts = Counter(data)
        mode = max(counts, key=counts.get)
        return mode
    
    def standard_deviation(data):
        #the standard deviation
        mean = Statistics.mean(data)
        squared_diffs = [(x - mean) ** 2 for x in data]
        variance = sum(squared_diffs) / len(data)
        return round(variance ** 0.5, 2)
    


    


print('Count:', len(ages)) 
print('Sum: ', sum(ages) )
print('Min: ', min(ages))
print('Max: ', max(ages))
print('Range: ',max(ages)-min(ages) ) 
print('Mean: ', Statistics.mean(ages)) 
print('Median: ', Statistics.median(ages)) 
print('Mode: ', Statistics.mode(ages) ) 
print('Standard Deviation: ', Statistics.standard_deviation(ages)) 
