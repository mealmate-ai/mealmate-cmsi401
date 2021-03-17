//
//import Foundation
//import SwiftUI
//
//public struct PieChartSlide: View {
//    var geometry: GeometryProxy
//    var nutData: NutData
//
//    var path: Path {
//        let chartSize = geometry.size.width
//        let radius = chartSize / 2
//        let centerX = radius
//        let centerY = radius
//
//        var path = Path()
//        path.move(to: CGPoint(x: centerX, y: centerY))
//        path.addArc(center: CGPoint(x: centerX, y: centerY),
//                    radius: radius,
//                    startAngle: nutData.startAngle,
//                    endAngle: nutData.endAngle,
//                    clockwise: false)
//        return path
//    }
//
//    public var body: some View {
//        path.fill(nutData.data.color)
//            .overlay(path.stroke(Color.white, lineWidth: 1))
//    }
//}

//startAngle: .degrees(-70), endAngle: .degrees(30))

//struct PieChartSlide_Previews: PreviewProvider {
//    static var previews: some View {
//        GeometryReader { geometry in
//            PieChartSlide(geometry: geometry, nutData: NutData())}
//    }
//}
