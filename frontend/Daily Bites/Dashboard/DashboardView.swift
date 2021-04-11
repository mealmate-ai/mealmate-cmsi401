import SwiftUI
import UIKit
import Combine

struct DashboardView: View {
    
    let pieChartData = NutPieChart(pieChartData: PieChartData(data: [1, 2]))
    
    var body: some View {
        
        //DESIGN ---------------------------------
        ZStack{
            VStack {
                Rectangle()
                    .fill(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
                    .frame(width: 419, height: 120)
                    .overlay(Text("Trends")
                        .fontWeight(.regular)
                        .font(.custom("Hiragino Sans W3", size: 34))
                        .foregroundColor(.white)
                                .offset(y: 20)
                        , alignment:
                    .center)

                HStack {
                    Button(action: {print("Day")}) {
                        Text("Day")
                            .fontWeight(.regular)
                            .font(.custom("Hiragino Sans W3", size: 22))
                            .foregroundColor(.gray)
                            .padding(25)
                    }
                    Button(action: {print("Week")}) {
                        Text("Week")
                            .fontWeight(.regular)
                            .font(.custom("Hiragino Sans W3", size: 23))
                            .foregroundColor(.gray)
                            .padding(25)
                    }
                    Button(action: {print("Month")}) {
                        Text("Month")
                            .fontWeight(.regular)
                            .font(.custom("Hiragino Sans W3", size: 22))
                            .foregroundColor(.gray)
                            .padding(25)
                    }
                }
                Rectangle()
                    .fill(Color.gray)
                    .frame(width: 425, height: 2)
                
                HStack (alignment: .center, spacing: 0, content:{
                    Text("Hello, Lexi!")
                        .fontWeight(.regular)
                        .font(.custom("Hiragino Sans W3", size: 33))
                        .foregroundColor(.gray)
                        .padding(20)
                        .lineLimit(nil)
                        .frame(width: 250, height: 70, alignment: .trailing)
                Spacer()
                })
                
                pieChartData
                    .frame(width: 400, height: 400, alignment: .trailing)
                    .offset(x: 20)
                
                Spacer()
                
            }
        }
    }
}
    
    struct DashboardView_Previews: PreviewProvider {
        static var previews: some View {
            DashboardView()
                .background(Color(.systemBackground))
                .edgesIgnoringSafeArea(.top)
        }
    }
