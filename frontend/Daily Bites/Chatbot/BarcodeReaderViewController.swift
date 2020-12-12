//
//import SwiftUI
//import UIKit
//import AVFoundation
//
////import PromiseKit
////import Alamofire
////import SwiftyJSON
//
//class BarcodeReaderViewController: UIViewController, AVCaptureMetadataOutputObjectsDelegate {
//    
//    var session: AVCaptureSession!
//    var previewLayer: AVCaptureVideoPreviewLayer!
//    
//    override func viewWillAppear(_ animated: Bool) {
//        super.viewWillAppear(animated)
//        if (session?.isRunning == false) { session.startRunning() }
//    }
//    
//    override func viewWillDisappear(_ animated: Bool) {
//        super.viewWillDisappear(animated)
//        if (session?.isRunning == true) { session.stopRunning() }
//    }
//    
//    override func viewDidLoad() {
//        super.viewDidLoad()
//        self.view.addGestureRecognizer(UITapGestureRecognizer(target: self, action: #selector(BarcodeReaderViewController.exit)))
//        
//        // Session
//        session = AVCaptureSession()
//        
//        // Capture Device
//        let videoCaptureDevice = AVCaptureDevice.defaultDevice(withMediaType: AVMediaTypeVideo)
//        
//        // Input
//        let videoInput: AVCaptureDeviceInput?
//        do {
//            videoInput = try AVCaptureDeviceInput(device: videoCaptureDevice)
//        } catch {
//            scanningNotPossible()
//            return
//        }
//        
//        if (session.canAddInput(videoInput!)) {
//            session.addInput(videoInput!)
//        } else {
//            scanningNotPossible()
//            return
//        }
//        
//        // Output
//        let metadataOutput = AVCaptureMetadataOutput()
//        if (session.canAddOutput(metadataOutput)) {
//            session.addOutput(metadataOutput)
//            metadataOutput.setMetadataObjectsDelegate(self, queue: DispatchQueue.main)
//            metadataOutput.metadataObjectTypes = metadataOutput.availableMetadataObjectTypes
//        } else {
//            scanningNotPossible()
//            return
//        }
//        
//        // Video preview
//        previewLayer = AVCaptureVideoPreviewLayer(session: session)
//        previewLayer.frame = view.layer.bounds
//        previewLayer.videoGravity = AVLayerVideoGravityResizeAspectFill
//        view.layer.addSublayer(previewLayer)
//        
//        //begin session
//        session.startRunning()
//        
//    }
//    
//    func scanningNotPossible() {
//        let alert = UIAlertController(title: Constants.BARCODE_ERROR_ALERT_TITLE, message: Constants.BARCODE_ERROR_ALERT_MESSAGE, preferredStyle: .alert)
//        alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
//        present(alert, animated: true, completion: nil)
//        session = nil
//    }
//    
//    func captureOutput(_ output: AVCaptureOutput!, didOutputMetadataObjects metadataObjects: [Any]!, from connection: AVCaptureConnection!) {
//        if let barcodeData = metadataObjects.first {
//            if let readableData = barcodeData as? AVMetadataMachineReadableCodeObject {
//                foundBarcode(readableData.stringValue!)
//            }
//            AudioServicesPlaySystemSound(SystemSoundID(kSystemSoundID_Vibrate))
//            session.stopRunning()
//        }
//    }
//    
//    func foundBarcode(_ barcode: String) {
//        // query server for barcode
//        var newBarcode = barcode
//        if barcode.count == 13 && barcode[barcode.startIndex] == "0" {
//            newBarcode = barcode.substring(from: barcode.index(barcode.startIndex, offsetBy: 1))
//        }
//        
//        _ = LanaLanguageProcessingService.sharedInstance.queryBarcode(_: newBarcode).then { food -> Promise<MessagePayload> in
//            print(food)
//            print(food.count)
//            
//            if food.count == 0 {
//                LanaBot.shared.sendMessage(text: LanaMessageBank.FOOD_ENTRY_BARCODE)
//                
//                return Promise(value: .text(content: LanaMessageBank.FOOD_ENTRY_NO_FOOD_ITEMS))
//            }
//            
//            // get new meal ID, or use mealInProgress ID
//            _ = LanaLanguageProcessingService.sharedInstance.getMealID(currMeal: LanaBot.shared.mealInProgress).then { mealID -> Promise<MessagePayload> in
//                LanaBot.shared.mealInProgress.mealID = Int64(mealID)
//                
//                let todayMeals = MealManager.shared.todayMeals()
//                if todayMeals.count == 0 {
//                    LanaBot.shared.delegate?.updateStreak()
//                }
//                
//                // add new food to current meal
//                let foodItem = NewLanaLanguageProcessingParser.parseFoodItem(food, mealID: mealID)
//                foodItem?.foodText = foodItem!.title!.lowercased()
//                let quant = String(describing: foodItem!.quantity)
//                let unit = foodItem?.chosenUnit?.label
//                let quantMessage = "Did you have " + quant + " " + unit! + "? If not, tell me how much you ate (or fix the quantity in Review)!"
//                
//                // get logID by calling new_log()
//                let payloadPromise = LanaLanguageProcessingService.sharedInstance.getLogID(mealID: mealID, rawText: "barcode: "+foodItem!.title!).then { logID -> Promise<MessagePayload> in
//                    foodItem?.logID = String(logID)
//                    // add new food to meal on server
//                    if (LanaBot.shared.debugMode == false) {
//                        LanaLanguageProcessingService.sharedInstance.addNewFood(meal: LanaBot.shared.mealInProgress, rowNum: LanaBot.shared.mealInProgress.foodItems!.count, item: foodItem!)
//                    }
//                    // prepend food item to list of foodItems
//                    LanaBot.shared.mealInProgress.insertIntoFoodItems(foodItem!, at: 0)
//                    MealManager.shared.save()
//                    
//                    // update local meal database by adding new meal or appending to existing meal
//                    if logID == 0 {
//                        print("logID == 0, assign meal to mealInProgress")
//                        //MealManager.shared.addMeal(meal: LanaBot.shared.mealInProgress)
//                    }
//                
//                    return Promise(value: .meal(meal: LanaBot.shared.mealInProgress))
//                    }.recover { error -> Promise<MessagePayload> in
//                        print(error)
//                        return Promise(value: .text(content: LanaMessageBank.FOOD_ENTRY_NO_INTERNET_CONNECTION))
//                }
//                Conversation.shared.sendMessage(message: Message(sender: .lana), payload: payloadPromise)
//                LanaBot.shared.sendMessage(text: quantMessage)
//                LanaBot.shared.prevBarcode = foodItem!.id
//                
//                return Promise(value: .meal(meal: LanaBot.shared.mealInProgress))
//                
//                }.recover { error -> Promise<MessagePayload> in
//                    switch (error) {
//                    case LanguageProcessingError.noFoodItems:
//                        return Promise(value: .text(content: LanaMessageBank.FOOD_ENTRY_NO_FOOD_ITEMS))
//                    case LanguageProcessingError.noInternet:
//                        return Promise(value: .text(content: LanaMessageBank.FOOD_ENTRY_NO_INTERNET_CONNECTION))
//                    default:
//                        assert(false)
//                    }
//                    
//                    return Promise(value: .text(content: LanaMessageBank.FOOD_ENTRY_NO_INTERNET_CONNECTION))
//            }
//
//            return Promise(value: .text(content: "got barcode food item"))
//            
//        }.recover { error -> Promise<MessagePayload> in
//                LanaBot.shared.sendMessage(text: LanaMessageBank.FOOD_ENTRY_NO_FOOD_ITEMS)
//                return Promise(value: .text(content: LanaMessageBank.FOOD_ENTRY_NO_FOOD_ITEMS))
//        }
//
//        let alert = UIAlertController(title: "Found barcode", message: barcode, preferredStyle: UIAlertControllerStyle.alert)
//        alert.addAction(UIAlertAction(title: "OK", style: .default, handler: { _ in
//            self.dismiss(animated: true, completion: nil)
//        }))
//        present(alert, animated: true, completion: nil)
//    }
//    
//    func exit() {
//        self.dismiss(animated: true, completion: nil)
//    }
//}
//
//
