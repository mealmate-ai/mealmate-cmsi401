//import SwiftUI
//import UIKit
//
//struct CuisinesDropDown: View {
//    @State var expand = false
//    var body: some View{
//        VStack() {
//            VStack(){
//                HStack(){
//                    Text("Cuisines")
//                        .foregroundColor(.gray)
//                        .padding(.bottom, 5)
//                    Image(systemName: expand ? "chevron.up" : "chevron.down")
//                        .resizable()
//                        .frame(width: 10, height: 10)
//                        .foregroundColor(.gray)
//                }.onTapGesture {
//                    self.expand.toggle()
//                }
//                if expand{
//                    Button(action: {
//                        print("1")
//                        self.expand.toggle()
//                    }) {
//                        Text("African")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("2")
//                        self.expand.toggle()
//                    }) {
//                        Text("American")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("3")
//                        self.expand.toggle()
//                    }) {
//                        Text("British")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("4")
//                        self.expand.toggle()
//                    }) {
//                        Text("Cajun")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("5")
//                        self.expand.toggle()
//                    }) {
//                        Text("Caribbean")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("6")
//                        self.expand.toggle()
//                    }) {
//                        Text("Chinese")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("7")
//                        self.expand.toggle()
//                    }) {
//                        Text("Eastern European")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("8")
//                        self.expand.toggle()
//                    }) {
//                        Text("European")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("9")
//                        self.expand.toggle()
//                    }) {
//                        Text("French")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("10")
//                        self.expand.toggle()
//                    }) {
//                        Text("German")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("11")
//                        self.expand.toggle()
//                    }) {
//                        Text("Greek")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("12")
//                        self.expand.toggle()
//                    }) {
//                        Text("Indian")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("13")
//                        self.expand.toggle()
//                    }) {
//                        Text("Irish")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("14")
//                        self.expand.toggle()
//                    }) {
//                        Text("Italian")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("15")
//                        self.expand.toggle()
//                    }) {
//                        Text("Japanese")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("16")
//                        self.expand.toggle()
//                    }) {
//                        Text("Jewish")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("17")
//                        self.expand.toggle()
//                    }) {
//                        Text("Korean")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("18")
//                        self.expand.toggle()
//                    }) {
//                        Text("Latin American")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("19")
//                        self.expand.toggle()
//                    }) {
//                        Text("Mediterranean")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("20")
//                        self.expand.toggle()
//                    }) {
//                        Text("Mexican")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("21")
//                        self.expand.toggle()
//                    }) {
//                        Text("Middle Eastern")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("22")
//                        self.expand.toggle()
//                    }) {
//                        Text("Nordic")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("23")
//                        self.expand.toggle()
//                    }) {
//                        Text("Southern")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("24")
//                        self.expand.toggle()
//                    }) {
//                        Text("Spanish")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("25")
//                        self.expand.toggle()
//                    }) {
//                        Text("Thai")
//                            .padding(10)
//                    }
//                    Button(action: {
//                        print("25")
//                        self.expand.toggle()
//                    }) {
//                        Text("Vietnamese")
//                            .padding(10)
//                    }
//                }
//                .padding()
//                    .cornerRadius(15)
//                    .shadow(color: .gray, radius: 3)
//                    .animation(.spring())
//            }
//        }
//    }
//}
