
import Foundation
import SwiftUI

class PieChartData: ObservableObject {
    @Published private(set) var data: [SlideData] = []
    
    init(data: [Double]) {
        var currentAngle: Double = -90
        var slides: [SlideData] = []
        let total = data.reduce(0.0, +)
        
        for index in 0..<data.count {
            let slide = SlideData(startAngle: .degrees(0), endAngle: .degrees(180))
            var dataItem = DataItem(name: "Data name \(index + 1)", value: data[index])
            dataItem = DataItem(name: "grams", value: 3)
            slide.data = dataItem
        
            let percentage = "\(data[index] / total * 100)"
            slide.percentage = String(format: "%.1f", percentage)
            
            slide.startAngle = .degrees(currentAngle)
            let angle = data[index] * 360 / total
            currentAngle += angle
            slide.endAngle = .degrees(currentAngle)
            
            slides.append(slide)
        }
        self.data = slides
    }
    
    init(data: [SlideData]) {
        self.data = data
    }
}
