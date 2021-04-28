
import SwiftUI
import Combine

struct NutPieChart: View {
    
    var pieChartData: PieChartData
    
    var body: some View {
        GeometryReader { geometry in
            self.makePieChart(geometry, pieChartData: self.pieChartData.data)
        }
    }
    
    func makePieChart(_ geometry: GeometryProxy, pieChartData: [SlideData]) -> some View {
        return ZStack {
            ForEach(0..<pieChartData.count, id: \.self) { index in
                PieChartSlide(geometry: geometry, slideData: pieChartData[index], index: index)
            }
        }
//        ForEach(slides) { SlideData in
//                       Text("\(SlideData.annotation) grams")
//                           .foregroundColor(Color.white)
//                   }
        }
}

struct PieChart_Previews: PreviewProvider {
    static var previews: some View {
        NutPieChart(pieChartData: PieChartData(data: [1, 2]))
    }
}
