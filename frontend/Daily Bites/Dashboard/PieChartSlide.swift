
import Foundation
import SwiftUI

public struct PieChartSlide: View {
    var geometry: GeometryProxy
    var slideData: SlideData
    
    var path: Path {
        let chartSize = geometry.size.width * 0.90
        let radius = chartSize / 2
        let centerX = radius
        let centerY = radius
        
        var path = Path()
        path.move(to: CGPoint(x: centerX, y: centerY))
        path.addArc(center: CGPoint(x: centerX, y: centerY),
                    radius: radius,
                    startAngle: slideData.startAngle,
                    endAngle: slideData.endAngle,
                    clockwise: false)
        return path
    }
    
    public var body: some View {
        path.fill(slideData.data.color)
            .overlay(path.stroke(Color.white, lineWidth: 2))
    }
}

struct PieChartSlide_Previews: PreviewProvider {
    static var previews: some View {
        GeometryReader { geometry in
            PieChartSlide(geometry: geometry, slideData: SlideData())
        }
    }
}
