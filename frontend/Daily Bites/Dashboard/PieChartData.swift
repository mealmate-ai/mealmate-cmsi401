//
//import Foundation
//import SwiftUI
//import UIKit
//
//class PieChartData: ObservableObject {
//    @Published private(set) var data: [NutData] = []
//
//    init(data: [Double]) {
//        var currentAngle: Double = -90
//        var slides: [NutData] = []
//        let total = data.reduce(0.0, +)
//
//        for index in 0..<data.count {
//            let nut_slide = NutData()
//            nut_slide.data = NutItem(name: "Data name \(index + 1)", value: data[index])
            
//            let percentage = data[index] / total * 100
//            nut_slide.percentage = String(format: "%.1f", percentage)
            
//            nut_slide.startAngle = .degrees(currentAngle)
//            let angle = data[index] * 360 / total
//            currentAngle += angle
//            nut_slide.endAngle = .degrees(currentAngle)
//
//            slides.append(nut_slide)
//        }
//        self.data = slides
//    }
//
//    init(data: [NutData]) {
//        self.data = data
//    }
//}
