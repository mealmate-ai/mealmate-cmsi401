
import SwiftUI
//import UIKit

struct ContentView: View {
    
    var body: some View {
        NavigationView{
            
            TabView{
                
                DashboardView()
                    .padding(.top, -30)
                    .tabItem {
                        VStack {
                            Image(systemName: "chart.bar")
                            Text("Dashboard")
                        }
                }
                
                ChatView()
                    .padding(.top, -30)
                    .tabItem {
                        VStack {
                            Image(systemName: "text.bubble")
                            Text("Chat")
                        }
                }
                
                RecipesView()
                    .padding(.top, -30)
                    .tabItem {
                        VStack {
                            Image(systemName: "book")
                            Text("Recipes")
                        }
                }
                
                SettingsView()
                    .padding(.top, -30)
                    .tabItem {
                        VStack {
                            Image(systemName: "gear")
                            Text("Settings")
                        }
                }
                
                //Spacer()
            }
        }.navigationBarHidden(true)
        .navigationBarTitle("")
    }
    
    
    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            ContentView()
                .edgesIgnoringSafeArea([.top])
            .border(Color.purple)
                .background(Color(.systemBackground))
        }
    }
}

