//import SwiftUI
//import UIKit
//
//protocol DateRangeSpecifierViewDelegate: class {
//    func dateRangeSpecifier(_ dateRangeSpecifier: DateRangeSpecifierView, didChooseDateRange dateRange: Int)
//    func dateRangeSpecifier(_ dateRangeSpecifier: DateRangeSpecifierView, didChooseDate date: Date)
//}
//
//enum DateRange: Int {
//    case singleDay = 0
//    case week = 7
//    case thirtyDays = 30
//}
//
//class DateRangeSpecifierView: UIView {
//
//    // MARK: - Properties -
//
//    weak var delegate: DateRangeSpecifierViewDelegate?
//
//    var chosenDateRange: DateRange = .singleDay {
//        didSet {
//            self.delegate?.dateRangeSpecifier(self, didChooseDateRange: self.chosenDateRange.rawValue)
//            self.highlightAppropriateButton()
//        }
//    }
//
//    var isEditing = false
//    let datePicker = UIDatePicker()
//
//    // views
//    @IBOutlet var singleDayButton: UIButton!
//    @IBOutlet var weekButton: UIButton!
//    @IBOutlet var thirtyDaysButton: UIButton!
//    @IBOutlet var datePickerButton: UITextField!
//
//    fileprivate lazy var allButtons: [UIButton] = {
//        return [self.singleDayButton, self.weekButton, self.thirtyDaysButton]
//    }()
//
//
//    override func awakeFromNib() {
//        super.awakeFromNib()
//        self.setUp()
//    }
//
//    fileprivate func setUp() {
//
//        // background colors
//        self.backgroundColor = UIColor.clear
//
//        // corner radius
//        self.allButtons.forEach { button in
//            button.layer.cornerRadius = 3.0
//        }
//
//        // date picker and button
//        self.datePicker.datePickerMode = .date
//        self.datePicker.addTarget(self, action: #selector(DateRangeSpecifierView.didChangeDate(_:)), for: .valueChanged)
//        self.datePicker.setDate(Date(), animated: false)
//        self.datePicker.maximumDate = Date()
//        self.datePickerButton.inputView = self.datePicker
//        self.datePickerButton.backgroundColor = .clear
//        self.datePickerButton.tintColor = .clear
//        self.datePickerButton.borderStyle = .none
//    }
//
//    // MARK: - Button Actions -
//
//    @IBAction func didPressMealTypeButton(_ sender: UIButton) {
//        switch sender {
//        case self.singleDayButton:
//            self.chosenDateRange = .singleDay
//        case self.weekButton:
//            self.chosenDateRange = .week
//            //self.datePicker.maximumDate = Date().addingTimeInterval(-7*60*60*24)
//        case self.thirtyDaysButton:
//            self.chosenDateRange = .thirtyDays
//            //self.datePicker.maximumDate = Date().addingTimeInterval(-30*60*60*24)
//        default:
//            assert(false)
//            break
//        }
//    }
//
//    @objc fileprivate func didChangeDate(_ sender: UIDatePicker) {
//        self.delegate?.dateRangeSpecifier(self, didChooseDate: sender.date)
//    }
//
//    fileprivate func highlightAppropriateButton() {
//
//        var buttonToHighlight: UIButton?
//
//        switch self.chosenDateRange {
//        case .singleDay:
//            buttonToHighlight = self.singleDayButton
//        case .week:
//            buttonToHighlight = self.weekButton
//        case .thirtyDays:
//            buttonToHighlight = self.thirtyDaysButton
//        }
//
//        self.allButtons.forEach { button in
//            if buttonToHighlight == button {
//                button.backgroundColor = Theme.MAIN_RED_THEME_COLOR
//                button.setTitleColor(UIColor.white, for: UIControlState())
//            } else {
//                button.backgroundColor = UIColor.clear
//                button.setTitleColor(UIColor.black, for: UIControlState())
//            }
//        }
//    }
//}
//
