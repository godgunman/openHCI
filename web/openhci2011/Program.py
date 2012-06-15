# -*- coding: utf-8 -*-
import os

from google.appengine.dist import use_library
use_library("django", "1.2")
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from openhci2011.Constants import debugMode

addressInfo = [ {"date":" 7/4",
                 "pureDate": "74",
                 "content": [{"addressTitle": "學員報到",
                              "addressTitleEn": "Check-in",
                              "addressTime": "08:30 - 09:00",
                              "short": True
                              },
                             {"addressTitle": "工作坊開始",
                              "addressTitleEn": "Opening",
                              "addressTime": "09:00 - 09:05",
                              "short": True
                              },
                             {"addressTitle": "開幕致詞:台大網媒所與此活動的促成",
                              "addressTitleEn": "Opening Remarks: NTU GINM and OpenHCI",
                              "addressTime": "09:05 - 09:15",
                              "speakers": [
                                           {"speakerName": "洪一平 Yi-Ping Hung",
                                            "speakerJob": ["台灣大學網媒所 所長"],
                                            "speakerJobEn": ["Chairman, Graduate Institute of Networking and Multimedia, NTU"],
                                            "speakerImage": "/2011/images/person/hyp.jpg"}
                                           ]
                              },
                             {"addressTitle": "開幕演說:關於跨領域合作,設計與工程之間",
                              "addressTitle": "Opening Talk: Design + Technology for Radical Innovation",
                              "addressTime": "09:15 - 09:25",
                              "speakers": [
                                           {"speakerName": "陳玲鈴 Lin-Lin Chen",
                                            "speakerJob": ["台灣科技大學工設系 教授"],
                                            "speakerJobEn": ["Professor, Dept. of Industrial and Commercial Design, NTUST"],
                                            "speakerImage": "/2011/images/person/cll.jpg"}
                                           ]
                              },
                             {"addressTitle": "TALK/Overview of Human-Computer Interaction",
                              "addressTime": "09:35 - 10:20",
                              "passport": True,
                              "speakers": [{"speakerName": "陳彥仰 Mike Chen",
                                            "speakerJob": ["台灣大學資工系 助理教授"],
                                            "speakerJobEn": ["Assistant Professor, Dept. of Computer Science and Information Engineering, NTU"],
                                            "speakerImage": "/2011/images/person/mc.png",
                                            "speakerPage": "http://mikechen.com/"}
                                           ],
                              "talk": True
                              },
                             {"addressTitle": "Q&A",
                              "addressTime": "10:20 - 10:35",
                              "short": True
                              },
                             {"addressTitle": "TALK/Brainstorming & Context Mapping",
                              "addressTime": "11:00 - 11:45",
                              "speakers": [{"speakerName": "莊雅量 Ya-Liang Chuang",
                                            "speakerJob": ["台灣科技大學工設系 老師"],
                                            "speakerJobEn": ["Teacher, Dept. of Industrial and Commercial Design, NTUST"],
                                            "speakerImage": "/2011/images/person/cyl.jpg"}
                                           ],
                              "talk": True
                              },
                             {"addressTitle": "Q&A",
                              "addressTime": "11:45 - 12:00",
                              "short": True
                              },
                             {"addressTitle": "Exercise/ Brainstorming 實戰",
                              "addressTitleEn": "Exercise/ Brainstorming",
                              "addressTime": "11:50 - 12:30",
                              "short": True
                              },
                             {"addressTitle": "TALK/Field Observation",
                              "addressTime": "13:30 - 14:15",
                              "passport": True,
                              "speakers": [{"speakerName": "蔡志浩 Chih-Hao Tsai",
                                            "speakerJob": ["高雄醫大心理系 助理教授"],
                                            "speakerJobEn": ["Assistant Professor, Dept. of Psychology, KMU"],
                                            "speakerImage": "/2011/images/person/tch.png",
                                            "speakerPage": "http://taiwan.chtsai.org/"}
                                           ],
                              "talk": True
                              },
                             {"addressTitle": "Q&A",
                              "addressTime": "14:15 - 14:30",
                              "short": True
                              },
                             {"addressTitle": "Exercise/ Observation 實戰",
                              "addressTitleEn": "Exercise/ Observation",
                              "addressTime": "14:30 - 16:00",
                              "short": True
                              },
                             {"addressTitle": "Exercise/ 快速原形製作",
                              "addressTitleEn": "Exercise/ Rapid prototyping",
                              "addressTime": "17:00 - 18:00",
                              "short": True
                              }
                            ],
                  "break": True
                 },
                 {"date": "7/5",
                  "pureDate": "75",
                  "content": [{"addressTitle": "TALK/Design Thinking",
                               "addressTime": "09:05 - 09:50",
                               "passport": True,
                               "speakers": [{"speakerName": "唐玄輝 Hsien-Hui Tang",
                                             "speakerJob": ["台灣科技大學工設系 副教授"],
                                             "speakerJobEn": ["Vice Professor, Dept. of Industrial and Commercial Design, NTUST"],
                                             "speakerImage": "/2011/images/person/thh.png",
                                             "speakerPage": "http://blog.drhhtang.net"}
                                            ],
                               "talk": True
                               },
                              {"addressTitle": "Q&A",
                              "addressTime": "09:50 - 10:05",
                              "short": True
                              },
                              {"addressTitle": "Exercise/使用者中心設計 實戰",
                               "addressTitleEn": "Exercise/ User-centered design",
                              "addressTime": "10:15 - 10:55",
                              "short": True
                              },
                              {"addressTitle": "TALK/Designing Affordance",
                               "addressTime": "11:30 - 12:15",
                               "passport": True,
                               "speakers": [{"speakerName": "唐聖凱 Sheng Kai Tang (Tony)",
                                             "speakerJob": ["華碩設計中心 使用者經驗設計專員"],
                                             "speakerJobEn": ["UX Designer, ASUS Design Center"],
                                             "speakerImage": "/2011/images/person/tt.png"}
                                            ],
                               "talk": True,
                               },
                              {"addressTitle": "Q&A",
                              "addressTime": "12:15 - 12:30",
                              "short": True
                              },
                              {"addressTitle": "TALK/Physical Computing 101",
                               "addressTime": "13:30 - 14:15",
                               "speakers": [{"speakerName": "許世樺  Ben Hsu",
                                             "speakerJob": ["藝科資訊 經理"],
                                             "speakerJobEn": ["Manager, Aroboto"],
                                             "speakerImage": "/2011/images/person/hb.jpg"}
                                            ],
                               "talk": True
                               },
                              {"addressTitle": "Q&A",
                              "addressTime": "14:15 - 14:30",
                              "short": True
                              },
                              {"addressTitle": "Exercise/互動原型 實戰",
                               "addressTitleEn": "Exercise/ Interactive prototyping",
                              "addressTime": "15:10 - 17:10",
                              "short": True
                              }
                              ],
                    "break": False
                  },
                  {"date": "7/6",
                   "pureDate": "76",
                   "content": [{"addressTitle": "TALK/Designing Interaction",
                                "addressTime": "09:05 - 09:50",
                                "passport": True,
                                "speakers": [{"speakerName": "梁容輝 Rung-Huei Liang",
                                              "speakerJob": ["台灣科技大學工設系 助理教授"],
                                              "speakerJobEn": ["Assistant Professor, Dept. of Industrial and Commercial Design, NTUST"],
                                              "speakerImage": "/2011/images/person/lrh.png",
                                              "speakerPage": "http://jazzliang.wordpress.com"}
                                             ],
                                "talk": True
                               },
                               {"addressTitle": "Q&A",
                               "addressTime": "09:50 - 10:05",
                               "short": True
                               },
                               {"addressTitle": "Exercise/互動腳本設計 實戰",
                                "addressTitle": "Exercise/ Interaction design",
                                  "addressTime": "10:15 - 10:55",
                                  "short": True
                                },
                               {"addressTitle": "TALK/Designing Usability Testing",
                                "addressTime": "11:30 -12:15",
                                "passport": True,
                                "speakers": [{"speakerName": "游牧民 Mumin Yu",
                                              "speakerJob": ["台大智活中心使用者經驗實驗室 主持人", "悠越互動顧問公司 首席顧問"],
                                              "speakerJobEn": ["Chairman, UX Lab of INSIGHT Center, NTU", "User Experience Consultant, USERXING"],
                                              "speakerImage": "/2011/images/person/ym.png"},
                                             {"speakerName": "王秀娟 Jen Wang",
                                              "speakerJob": ["台大智活中心使用者經驗實驗室 資深研究員"],
                                              "speakerJobEn": ["Researcher, UX Lab of INSIGHT Center, NTU"],
                                              "speakerImage": "/2011/images/person/wj.png"}
                                             ],
                                "talk": True,
                               },
                               {"addressTitle": "Q&A",
                                "addressTime": "12:15 - 12:30",
                                "short": True
                                },
                               {"addressTitle": "各組簡報作品大綱與使用者測試提案",
                                "addressTitle": "Proposal for usability testing",
                                "addressTime": "14:30 - 17:40"
                                }
                              ]
                   },
                   {"date": "7/7",
                    "pureDate": "77",
                    "content": [{"addressTitle": "Exercise/使用者測試 實戰",
                                 "addressTitle": "Exercise/ Usability testing",
                                  "addressTime": "09:05 - 12:30",
                                  "short": True
                                },
                                {"addressTitle": "TALK/Designing Human Factors",
                                 "addressTime": "13:30 - 14:15",
                                 "passport": True,
                                 "speakers": [{"speakerName": "盧禎慧 Chen-Hui, Lu",
                                               "speakerJob": ["實踐大學工設系 副教授"],
                                               "speakerJobEn": ["Vice Professor, Dept. of Industrial Design, Shih Chien Univ."],
                                               "speakerImage": "/2011/images/person/lch.png"}
                                              ],
                                 "talk": True
                                },
                                {"addressTitle": "Q&A",
                                 "addressTime": "14:15 - 14:30",
                                 "short": True
                                 },
                               ]
                   },
                   {"date": "7/8",
                    "pureDate": "78",
                    "content": [{"addressTitle": "各組成果報告",
                                 "addressTitleEn": "Final presentation",
                                 "addressTime": "13:00 - 13:50",
                                 "speakerEmpty": True
                                },
                                {"addressTitle": "互動展示",
                                 "addressTitleEn": "Interactive demo",
                                 "addressTime": "14:00 - 17:00",
                                 "speakerEmpty": True
                                },
                                {"addressTitle": "結業 頒獎典禮",
                                 "addressTitle": "Closing plenary",
                                 "addressTime": "17:30 - 18:30",
                                 "speakerEmpty": True
                                }
                               ]
                   }
              ]

class ProgramPage(webapp.RequestHandler):
    def get(self):
        language = self.request.get("l")
        if language == "":
            language = "zh_TW"
            
        pagePath = os.path.join(os.path.dirname(__file__), "html/program.html")
        pageDict = {"address":addressInfo, "language": language}
        self.response.out.write(template.render(pagePath, pageDict))
    
application = webapp.WSGIApplication([('/2011/program/', ProgramPage)], debug=debugMode)

def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
    main()
