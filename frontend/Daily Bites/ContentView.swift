
import SwiftUI
//import UIKit

struct ContentView: View {
    
    var body: some View {
        NavigationView{
            
            TabView{
                
                DashboardView()
                    .navigationBarHidden(true)
                    .padding(.top, -30)
                    .tabItem {
                        VStack {
                            Image(systemName: "chart.bar")
                            Text("Dashboard")
                        }
                }
                
                ChatView()
                    .navigationBarHidden(true)
                    .padding(.top, -30)
                    .tabItem {
                        VStack {
                            Image(systemName: "text.bubble")
                            Text("Chat")
                        }
                }
                
                RecipesView()
                    .navigationBarHidden(true)
                    .padding(.top, -30)
                    .tabItem {
                        VStack {
                            Image(systemName: "book")
                            Text("Recipes")
                        }
                }
                
                SettingsView()
                    .navigationBarHidden(true)
                    .padding(.top, -30)
                    .tabItem {
                        VStack {
                            Image(systemName: "gear")
                            Text("Settings")
                        }
                }
                
                //Spacer()
                
            }
        }
    }
    
    
    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            ContentView().edgesIgnoringSafeArea(.top)
        }
    }
}
