#!/usr/bin/env python3
# -*- coding:utf-8 -*-
##################################################################################
# File: /mnt/c/Projects/ANGA UTM/src/applications/bounding.py                    #
# Project: /mnt/c/Projects/ANGA UTM/src/applications                             #
# Created Date: Saturday, March 28th 2020, 1:51:07 pm                            #
# Author: Geoffrey Nyaga Kinyua ( <geoffrey@geoffreynyaga.com> )                 #
# -----                                                                          #
# Last Modified: Saturday March 28th 2020 8:38:58 pm                             #
# Modified By:  Geoffrey Nyaga Kinyua ( <geoffrey@geoffreynyaga.com> )           #
# -----                                                                          #
# Apache License                                                                 #
# Version 2.0, January 2004                                                      #
# http://www.apache.org/licenses/                                                #
#                                                                                #
# TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION                   #
#                                                                                #
# 1. Definitions.                                                                #
#                                                                                #
# "License" shall mean the terms and conditions for use, reproduction, and       #
# distribution as defined by Sections 1 through 9 of this document.              #
#                                                                                #
# "Licensor" shall mean the copyright owner or entity authorized by the copyright#
# owner that is granting the License.                                            #
#                                                                                #
# "Legal Entity" shall mean the union of the acting entity and all other entities#
# that control, are controlled by, or are under common control with that entity. #
# For the purposes of this definition, "control" means (i) the power, direct or  #
# indirect, to cause the direction or management of such entity, whether by      #
# contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the #
# outstanding shares, or (iii) beneficial ownership of such entity.              #
#                                                                                #
# "You" (or "Your") shall mean an individual or Legal Entity exercising          #
# permissions granted by this License.                                           #
#                                                                                #
# "Source" form shall mean the preferred form for making modifications, including#
# but not limited to software source code, documentation source, and             #
# configuration files.                                                           #
#                                                                                #
# "Object" form shall mean any form resulting from mechanical transformation or  #
# translation of a Source form, including but not limited to compiled object     #
# code, generated documentation, and conversions to other media types.           #
#                                                                                #
# "Work" shall mean the work of authorship, whether in Source or Object form,    #
# made available under the License, as indicated by a copyright notice that is   #
# included in or attached to the work (an example is provided in the Appendix    #
# below).                                                                        #
#                                                                                #
# "Derivative Works" shall mean any work, whether in Source or Object form, that #
# is based on (or derived from) the Work and for which the editorial revisions,  #
# annotations, elaborations, or other modifications represent, as a whole, an    #
# original work of authorship. For the purposes of this License, Derivative Works#
# shall not include works that remain separable from, or merely link (or bind by #
# name) to the interfaces of, the Work and Derivative Works thereof.             #
#                                                                                #
# "Contribution" shall mean any work of authorship, including the original       #
# version of the Work and any modifications or additions to that Work or         #
# Derivative Works thereof, that is intentionally submitted to Licensor for      #
# inclusion in the Work by the copyright owner or by an individual or Legal      #
# Entity authorized to submit on behalf of the copyright owner. For the purposes #
# of this definition, "submitted" means any form of electronic, verbal, or       #
# written communication sent to the Licensor or its representatives, including   #
# but not limited to communication on electronic mailing lists, source code      #
# control systems, and issue tracking systems that are managed by, or on behalf  #
# of, the Licensor for the purpose of discussing and improving the Work, but     #
# excluding communication that is conspicuously marked or otherwise designated in#
# writing by the copyright owner as "Not a Contribution."                        #
#                                                                                #
# "Contributor" shall mean Licensor and any individual or Legal Entity on behalf #
# of whom a Contribution has been received by Licensor and subsequently          #
# incorporated within the Work.                                                  #
#                                                                                #
# 2. Grant of Copyright License. Subject to the terms and conditions of this     #
# License, each Contributor hereby grants to You a perpetual, worldwide,         #
# non-exclusive, no-charge, royalty-free, irrevocable copyright license to       #
# reproduce, prepare Derivative Works of, publicly display, publicly perform,    #
# sublicense, and distribute the Work and such Derivative Works in Source or     #
# Object form.                                                                   #
#                                                                                #
# 3. Grant of Patent License. Subject to the terms and conditions of this        #
# License, each Contributor hereby grants to You a perpetual, worldwide,         #
# non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this  #
# section) patent license to make, have made, use, offer to sell, sell, import,  #
# and otherwise transfer the Work, where such license applies only to those      #
# patent claims licensable by such Contributor that are necessarily infringed by #
# their Contribution(s) alone or by combination of their Contribution(s) with the#
# Work to which such Contribution(s) was submitted. If You institute patent      #
# litigation against any entity (including a cross-claim or counterclaim in a    #
# lawsuit) alleging that the Work or a Contribution incorporated within the Work #
# constitutes direct or contributory patent infringement, then any patent        #
# licenses granted to You under this License for that Work shall terminate as of #
# the date such litigation is filed.                                             #
#                                                                                #
# 4. Redistribution. You may reproduce and distribute copies of the Work or      #
# Derivative Works thereof in any medium, with or without modifications, and in  #
# Source or Object form, provided that You meet the following conditions:        #
#                                                                                #
#      (a) You must give any other recipients of the Work or Derivative Works a  #
# copy of this License; and                                                      #
#                                                                                #
#      (b) You must cause any modified files to carry prominent notices stating  #
# that You changed the files; and                                                #
#                                                                                #
#      (c) You must retain, in the Source form of any Derivative Works that You  #
# distribute, all copyright, patent, trademark, and attribution notices from the #
# Source form of the Work, excluding those notices that do not pertain to any    #
# part of the Derivative Works; and                                              #
#                                                                                #
#      (d) If the Work includes a "NOTICE" text file as part of its distribution,#
# then any Derivative Works that You distribute must include a readable copy of  #
# the attribution notices contained within such NOTICE file, excluding those     #
# notices that do not pertain to any part of the Derivative Works, in at least   #
# one of the following places: within a NOTICE text file distributed as part of  #
# the Derivative Works; within the Source form or documentation, if provided     #
# along with the Derivative Works; or, within a display generated by the         #
# Derivative Works, if and wherever such third-party notices normally appear. The#
# contents of the NOTICE file are for informational purposes only and do not     #
# modify the License. You may add Your own attribution notices within Derivative #
# Works that You distribute, alongside or as an addendum to the NOTICE text from #
# the Work, provided that such additional attribution notices cannot be construed#
# as modifying the License.                                                      #
#                                                                                #
#      You may add Your own copyright statement to Your modifications and may    #
# provide additional or different license terms and conditions for use,          #
# reproduction, or distribution of Your modifications, or for any such Derivative#
# Works as a whole, provided Your use, reproduction, and distribution of the Work#
# otherwise complies with the conditions stated in this License.                 #
#                                                                                #
# 5. Submission of Contributions. Unless You explicitly state otherwise, any     #
# Contribution intentionally submitted for inclusion in the Work by You to the   #
# Licensor shall be under the terms and conditions of this License, without any  #
# additional terms or conditions. Notwithstanding the above, nothing herein shall#
# supersede or modify the terms of any separate license agreement you may have   #
# executed with Licensor regarding such Contributions.                           #
#                                                                                #
# 6. Trademarks. This License does not grant permission to use the trade names,  #
# trademarks, service marks, or product names of the Licensor, except as required#
# for reasonable and customary use in describing the origin of the Work and      #
# reproducing the content of the NOTICE file.                                    #
#                                                                                #
# 7. Disclaimer of Warranty. Unless required by applicable law or agreed to in   #
# writing, Licensor provides the Work (and each Contributor provides its         #
# Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY    #
# KIND, either express or implied, including, without limitation, any warranties #
# or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A    #
# PARTICULAR PURPOSE. You are solely responsible for determining the             #
# appropriateness of using or redistributing the Work and assume any risks       #
# associated with Your exercise of permissions under this License.               #
#                                                                                #
# 8. Limitation of Liability. In no event and under no legal theory, whether in  #
# tort (including negligence), contract, or otherwise, unless required by        #
# applicable law (such as deliberate and grossly negligent acts) or agreed to in #
# writing, shall any Contributor be liable to You for damages, including any     #
# direct, indirect, special, incidental, or consequential damages of any         #
# character arising as a result of this License or out of the use or inability to#
# use the Work (including but not limited to damages for loss of goodwill, work  #
# stoppage, computer failure or malfunction, or any and all other commercial     #
# damages or losses), even if such Contributor has been advised of the           #
# possibility of such damages.                                                   #
#                                                                                #
# 9. Accepting Warranty or Additional Liability. While redistributing the Work or#
# Derivative Works thereof, You may choose to offer, and charge a fee for,       #
# acceptance of support, warranty, indemnity, or other liability obligations     #
# and/or rights consistent with this License. However, in accepting such         #
# obligations, You may act only on Your own behalf and on Your sole              #
# responsibility, not on behalf of any other Contributor, and only if You agree  #
# to indemnify, defend, and hold each Contributor harmless for any liability     #
# incurred by, or claims asserted against, such Contributor by reason of your    #
# accepting any such warranty or additional liability.                           #
#                                                                                #
# END OF TERMS AND CONDITIONS                                                    #
#                                                                                #
# APPENDIX: How to apply the Apache License to your work.                        #
#                                                                                #
# To apply the Apache License to your work, attach the following boilerplate     #
# notice, with the fields enclosed by brackets "[]" replaced with your own       #
# identifying information. (Don't include the brackets!)  The text should be     #
# enclosed in the appropriate comment syntax for the file format. We also        #
# recommend that a file or class name and description of purpose be included on  #
# the same "printed page" as the copyright notice for easier identification      #
# within third-party archives.                                                   #
#                                                                                #
# Copyright [yyyy] [name of copyright owner]                                     #
#                                                                                #
# Licensed under the Apache License, Version 2.0 (the "License");                #
# you may not use this file except in compliance with the License.               #
# You may obtain a copy of the License at                                        #
#                                                                                #
# http://www.apache.org/licenses/LICENSE-2.0                                     #
#                                                                                #
# Unless required by applicable law or agreed to in writing, software            #
# distributed under the License is distributed on an "AS IS" BASIS,              #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.       #
# See the License for the specific language governing permissions and            #
# limitations under the License.                                                 #
# -----                                                                          #
# Copyright (c) 2020 ANGA UTM.                                                   #
##################################################################################


bounding_boxes = {
    "ABW": {
        "sw": {"lat": 12.1702998, "lon": -70.2809842},
        "ne": {"lat": 12.8102998, "lon": -69.6409842},
    },
    "AFG": {
        "sw": {"lat": 29.3772, "lon": 60.5176034},
        "ne": {"lat": 38.4910682, "lon": 74.889862},
    },
    "AGO": {
        "sw": {"lat": -18.038945, "lon": 11.4609793},
        "ne": {"lat": -4.3880634, "lon": 24.0878856},
    },
    "AIA": {
        "sw": {"lat": 18.0615454, "lon": -63.6391992},
        "ne": {"lat": 18.7951194, "lon": -62.7125449},
    },
    "ALA": {
        "sw": {"lat": 59.4541578, "lon": 19.0832098},
        "ne": {"lat": 60.87665, "lon": 21.3456556},
    },
    "ALB": {
        "sw": {"lat": 39.6448625, "lon": 19.1246095},
        "ne": {"lat": 42.6610848, "lon": 21.0574335},
    },
    "AND": {
        "sw": {"lat": 42.4288238, "lon": 1.4135781},
        "ne": {"lat": 42.6559357, "lon": 1.7863837},
    },
    "ANT": {
        "sw": {"lat": 12.1544542, "lon": -68.940593},
        "ne": {"lat": 12.1547472, "lon": -68.9403518},
    },
    "ARE": {
        "sw": {"lat": 22.6444, "lon": 51.498},
        "ne": {"lat": 26.2822, "lon": 56.3834},
    },
    "ARG": {
        "sw": {"lat": -55.1850761, "lon": -73.5600329},
        "ne": {"lat": -21.781168, "lon": -53.6374515},
    },
    "ARM": {
        "sw": {"lat": 38.8404775, "lon": 43.4471395},
        "ne": {"lat": 41.300712, "lon": 46.6333087},
    },
    "ASM": {
        "sw": {"lat": -14.7608358, "lon": -171.2951296},
        "ne": {"lat": -10.8449746, "lon": -167.9322899},
    },
    "ATA": {
        "sw": {"lat": -85.0511287, "lon": -180.0},
        "ne": {"lat": -60.0, "lon": 180.0},
    },
    "ATF": {
        "sw": {"lat": -50.2187169, "lon": 39.4138676},
        "ne": {"lat": -11.3139928, "lon": 77.8494974},
    },
    "ATG": {
        "sw": {"lat": 16.7573901, "lon": -62.5536517},
        "ne": {"lat": 17.929, "lon": -61.447857},
    },
    "AUS": {
        "sw": {"lat": -55.3228175, "lon": 72.2460938},
        "ne": {"lat": -9.0882278, "lon": 168.2249543},
    },
    "AUT": {
        "sw": {"lat": 46.3722761, "lon": 9.5307487},
        "ne": {"lat": 49.0205305, "lon": 17.160776},
    },
    "AZE": {
        "sw": {"lat": 38.3929551, "lon": 44.7633701},
        "ne": {"lat": 41.9502947, "lon": 51.0090302},
    },
    "BDI": {
        "sw": {"lat": -4.4693155, "lon": 29.0007401},
        "ne": {"lat": -2.3096796, "lon": 30.8498462},
    },
    "BEL": {
        "sw": {"lat": 49.4969821, "lon": 2.3889137},
        "ne": {"lat": 51.5516667, "lon": 6.408097},
    },
    "BEN": {
        "sw": {"lat": 6.0398696, "lon": 0.776667},
        "ne": {"lat": 12.4092447, "lon": 3.843343},
    },
    "BFA": {
        "sw": {"lat": 9.4104718, "lon": -5.5132416},
        "ne": {"lat": 15.084, "lon": 2.4089717},
    },
    "BGD": {
        "sw": {"lat": 20.3756582, "lon": 88.0075306},
        "ne": {"lat": 26.6382534, "lon": 92.6804979},
    },
    "BGR": {
        "sw": {"lat": 41.2353929, "lon": 22.3571459},
        "ne": {"lat": 44.2167064, "lon": 28.8875409},
    },
    "BHR": {
        "sw": {"lat": 25.535, "lon": 50.2697989},
        "ne": {"lat": 26.6872444, "lon": 50.9233693},
    },
    "BHS": {
        "sw": {"lat": 20.7059846, "lon": -80.7001941},
        "ne": {"lat": 27.4734551, "lon": -72.4477521},
    },
    "BIH": {
        "sw": {"lat": 42.5553114, "lon": 15.7287433},
        "ne": {"lat": 45.2764135, "lon": 19.6237311},
    },
    "BLM": {
        "sw": {"lat": 17.670931, "lon": -63.06639},
        "ne": {"lat": 18.1375569, "lon": -62.5844019},
    },
    "BLR": {
        "sw": {"lat": 51.2575982, "lon": 23.1783344},
        "ne": {"lat": 56.17218, "lon": 32.7627809},
    },
    "BLZ": {
        "sw": {"lat": 15.8857286, "lon": -89.2262083},
        "ne": {"lat": 18.496001, "lon": -87.3098494},
    },
    "BMU": {
        "sw": {"lat": 32.0469651, "lon": -65.1232222},
        "ne": {"lat": 32.5913693, "lon": -64.4109842},
    },
    "BOL": {
        "sw": {"lat": -22.8982742, "lon": -69.6450073},
        "ne": {"lat": -9.6689438, "lon": -57.453},
    },
    "BRA": {
        "sw": {"lat": -33.8689056, "lon": -73.9830625},
        "ne": {"lat": 5.2842873, "lon": -28.6341164},
    },
    "BRB": {
        "sw": {"lat": 12.845, "lon": -59.8562115},
        "ne": {"lat": 13.535, "lon": -59.2147175},
    },
    "BRN": {
        "sw": {"lat": 4.002508, "lon": 114.0758734},
        "ne": {"lat": 5.1011857, "lon": 115.3635623},
    },
    "BTN": {
        "sw": {"lat": 26.702016, "lon": 88.7464724},
        "ne": {"lat": 28.246987, "lon": 92.1252321},
    },
    "BVT": {
        "sw": {"lat": -54.654, "lon": 2.9345531},
        "ne": {"lat": -54.187, "lon": 3.7791099},
    },
    "BWA": {
        "sw": {"lat": -26.9059669, "lon": 19.9986474},
        "ne": {"lat": -17.778137, "lon": 29.375304},
    },
    "CAF": {
        "sw": {"lat": 2.2156553, "lon": 14.4155426},
        "ne": {"lat": 11.001389, "lon": 27.4540764},
    },
    "CAN": {
        "sw": {"lat": 41.6765556, "lon": -141.00275},
        "ne": {"lat": 83.3362128, "lon": -52.3231981},
    },
    "CCK": {
        "sw": {"lat": -12.4055983, "lon": 96.612524},
        "ne": {"lat": -11.6213132, "lon": 97.1357343},
    },
    "CHE": {
        "sw": {"lat": 45.817995, "lon": 5.9559113},
        "ne": {"lat": 47.8084648, "lon": 10.4922941},
    },
    "CHL": {
        "sw": {"lat": -56.725, "lon": -109.6795789},
        "ne": {"lat": -17.4983998, "lon": -66.0753474},
    },
    "CHN": {
        "sw": {"lat": 8.8383436, "lon": 73.4997347},
        "ne": {"lat": 53.5608154, "lon": 134.7754563},
    },
    "CIV": {
        "sw": {"lat": 4.1621205, "lon": -8.601725},
        "ne": {"lat": 10.740197, "lon": -2.493031},
    },
    "CMR": {
        "sw": {"lat": 1.6546659, "lon": 8.3822176},
        "ne": {"lat": 13.083333, "lon": 16.1921476},
    },
    "COD": {
        "sw": {"lat": -13.459035, "lon": 12.039074},
        "ne": {"lat": 5.3920026, "lon": 31.3056758},
    },
    "COG": {
        "sw": {"lat": -5.149089, "lon": 11.0048205},
        "ne": {"lat": 3.713056, "lon": 18.643611},
    },
    "COK": {
        "sw": {"lat": -22.15807, "lon": -166.0856468},
        "ne": {"lat": -8.7168792, "lon": -157.1089329},
    },
    "COL": {
        "sw": {"lat": -4.2316872, "lon": -82.1243666},
        "ne": {"lat": 16.0571269, "lon": -66.8511907},
    },
    "COM": {
        "sw": {"lat": -12.621, "lon": 43.025305},
        "ne": {"lat": -11.165, "lon": 44.7451922},
    },
    "CPV": {
        "sw": {"lat": 14.8031546, "lon": -25.3609478},
        "ne": {"lat": 17.2053108, "lon": -22.6673416},
    },
    "CRI": {
        "sw": {"lat": 5.3329698, "lon": -87.2722647},
        "ne": {"lat": 11.2195684, "lon": -82.5060208},
    },
    "CUB": {
        "sw": {"lat": 19.6275294, "lon": -85.1679702},
        "ne": {"lat": 23.4816972, "lon": -73.9190004},
    },
    "CXR": {
        "sw": {"lat": -10.5698515, "lon": 105.5336422},
        "ne": {"lat": -10.4123553, "lon": 105.7130159},
    },
    "CYM": {
        "sw": {"lat": 19.0620619, "lon": -81.6313748},
        "ne": {"lat": 19.9573759, "lon": -79.5110954},
    },
    "CYP": {
        "sw": {"lat": 34.4383706, "lon": 32.0227581},
        "ne": {"lat": 35.913252, "lon": 34.8553182},
    },
    "CZE": {
        "sw": {"lat": 48.5518083, "lon": 12.0905901},
        "ne": {"lat": 51.0557036, "lon": 18.859216},
    },
    "DEU": {
        "sw": {"lat": 47.2701114, "lon": 5.8663153},
        "ne": {"lat": 55.099161, "lon": 15.0419319},
    },
    "DJI": {
        "sw": {"lat": 10.9149547, "lon": 41.7713139},
        "ne": {"lat": 12.7923081, "lon": 43.6579046},
    },
    "DMA": {
        "sw": {"lat": 15.0074207, "lon": -61.6869184},
        "ne": {"lat": 15.7872222, "lon": -61.0329895},
    },
    "DNK": {
        "sw": {"lat": 54.4516667, "lon": 7.7153255},
        "ne": {"lat": 57.9524297, "lon": 15.5530641},
    },
    "DOM": {
        "sw": {"lat": 17.2701708, "lon": -72.0574706},
        "ne": {"lat": 21.303433, "lon": -68.1101463},
    },
    "DZA": {
        "sw": {"lat": 18.968147, "lon": -8.668908},
        "ne": {"lat": 37.2962055, "lon": 11.997337},
    },
    "ECU": {
        "sw": {"lat": -5.0159314, "lon": -92.2072392},
        "ne": {"lat": 1.8835964, "lon": -75.192504},
    },
    "EGY": {
        "sw": {"lat": 22.0, "lon": 24.6499112},
        "ne": {"lat": 31.8330854, "lon": 37.1153517},
    },
    "ERI": {
        "sw": {"lat": 12.3548219, "lon": 36.4333653},
        "ne": {"lat": 18.0709917, "lon": 43.3001714},
    },
    "ESH": {
        "sw": {"lat": 20.556883, "lon": -17.3494721},
        "ne": {"lat": 27.6666834, "lon": -8.666389},
    },
    "ESP": {
        "sw": {"lat": 27.4335426, "lon": -18.3936845},
        "ne": {"lat": 43.9933088, "lon": 4.5918885},
    },
    "EST": {
        "sw": {"lat": 57.5092997, "lon": 21.3826069},
        "ne": {"lat": 59.9383754, "lon": 28.2100175},
    },
    "ETH": {
        "sw": {"lat": 3.397448, "lon": 32.9975838},
        "ne": {"lat": 14.8940537, "lon": 47.9823797},
    },
    "FIN": {
        "sw": {"lat": 59.4541578, "lon": 19.0832098},
        "ne": {"lat": 70.0922939, "lon": 31.5867071},
    },
    "FJI": {
        "sw": {"lat": -21.9434274, "lon": 172.0},
        "ne": {"lat": -12.2613866, "lon": -178.5},
    },
    "FLK": {
        "sw": {"lat": -53.1186766, "lon": -61.7726772},
        "ne": {"lat": -50.7973007, "lon": -57.3662367},
    },
    "FRA": {
        "sw": {"lat": 41.2632185, "lon": -5.4534286},
        "ne": {"lat": 51.268318, "lon": 9.8678344},
    },
    "FRO": {
        "sw": {"lat": 61.3915553, "lon": -7.6882939},
        "ne": {"lat": 62.3942991, "lon": -6.2565525},
    },
    "FSM": {
        "sw": {"lat": 0.827, "lon": 137.2234512},
        "ne": {"lat": 10.291, "lon": 163.2364054},
    },
    "GAB": {
        "sw": {"lat": -4.1012261, "lon": 8.5002246},
        "ne": {"lat": 2.3182171, "lon": 14.539444},
    },
    "GBR": {
        "sw": {"lat": 49.674, "lon": -14.015517},
        "ne": {"lat": 61.061, "lon": 2.0919117},
    },
    "GEO": {
        "sw": {"lat": 41.0552922, "lon": 39.8844803},
        "ne": {"lat": 43.5864294, "lon": 46.7365373},
    },
    "GGY": {
        "sw": {"lat": 49.4155331, "lon": -2.6751703},
        "ne": {"lat": 49.5090776, "lon": -2.501814},
    },
    "GHA": {
        "sw": {"lat": 4.5392525, "lon": -3.260786},
        "ne": {"lat": 11.1748562, "lon": 1.2732942},
    },
    "GIB": {
        "sw": {"lat": 36.100807, "lon": -5.3941295},
        "ne": {"lat": 36.180807, "lon": -5.3141295},
    },
    "GIN": {
        "sw": {"lat": 7.1906045, "lon": -15.5680508},
        "ne": {"lat": 12.67563, "lon": -7.6381993},
    },
    "GLP": {
        "sw": {"lat": 15.8320085, "lon": -61.809764},
        "ne": {"lat": 16.5144664, "lon": -61.0003663},
    },
    "GMB": {
        "sw": {"lat": 13.061, "lon": -17.0288254},
        "ne": {"lat": 13.8253137, "lon": -13.797778},
    },
    "GNB": {
        "sw": {"lat": 10.6514215, "lon": -16.894523},
        "ne": {"lat": 12.6862384, "lon": -13.6348777},
    },
    "GNQ": {
        "sw": {"lat": -1.6732196, "lon": 5.4172943},
        "ne": {"lat": 3.989, "lon": 11.3598628},
    },
    "GRC": {
        "sw": {"lat": 34.7006096, "lon": 19.2477876},
        "ne": {"lat": 41.7488862, "lon": 29.7296986},
    },
    "GRD": {
        "sw": {"lat": 11.786, "lon": -62.0065868},
        "ne": {"lat": 12.5966532, "lon": -61.1732143},
    },
    "GRL": {
        "sw": {"lat": 59.515387, "lon": -74.1250416},
        "ne": {"lat": 83.875172, "lon": -10.0288759},
    },
    "GTM": {
        "sw": {"lat": 13.6345804, "lon": -92.3105242},
        "ne": {"lat": 17.8165947, "lon": -88.1755849},
    },
    "GUF": {
        "sw": {"lat": 2.112222, "lon": -54.60278},
        "ne": {"lat": 5.7507111, "lon": -51.6346139},
    },
    "GUM": {
        "sw": {"lat": 13.182335, "lon": 144.563426},
        "ne": {"lat": 13.706179, "lon": 145.009167},
    },
    "GUY": {
        "sw": {"lat": 1.1710017, "lon": -61.414905},
        "ne": {"lat": 8.6038842, "lon": -56.4689543},
    },
    "HKG": {
        "sw": {"lat": 22.1193278, "lon": 114.0028131},
        "ne": {"lat": 22.4393278, "lon": 114.3228131},
    },
    "HMD": {
        "sw": {"lat": -53.394741, "lon": 72.2460938},
        "ne": {"lat": -52.7030677, "lon": 74.1988754},
    },
    "HND": {
        "sw": {"lat": 12.9808485, "lon": -89.3568207},
        "ne": {"lat": 17.619526, "lon": -82.1729621},
    },
    "HRV": {
        "sw": {"lat": 42.1765993, "lon": 13.2104814},
        "ne": {"lat": 46.555029, "lon": 19.4470842},
    },
    "HTI": {
        "sw": {"lat": 17.9099291, "lon": -75.2384618},
        "ne": {"lat": 20.2181368, "lon": -71.6217461},
    },
    "HUN": {
        "sw": {"lat": 45.737128, "lon": 16.1138867},
        "ne": {"lat": 48.585257, "lon": 22.8977094},
    },
    "IDN": {
        "sw": {"lat": -11.2085669, "lon": 94.7717124},
        "ne": {"lat": 6.2744496, "lon": 141.0194444},
    },
    "IMN": {
        "sw": {"lat": 54.0539576, "lon": -4.7946845},
        "ne": {"lat": 54.4178705, "lon": -4.3076853},
    },
    "IND": {
        "sw": {"lat": 6.5546079, "lon": 68.1113787},
        "ne": {"lat": 35.6745457, "lon": 97.395561},
    },
    "IOT": {
        "sw": {"lat": -7.6454079, "lon": 71.036504},
        "ne": {"lat": -5.037066, "lon": 72.7020157},
    },
    "IRL": {
        "sw": {"lat": 51.222, "lon": -11.0133788},
        "ne": {"lat": 55.636, "lon": -5.6582363},
    },
    "IRN": {
        "sw": {"lat": 24.8465103, "lon": 44.0318908},
        "ne": {"lat": 39.7816502, "lon": 63.3332704},
    },
    "IRQ": {
        "sw": {"lat": 29.0585661, "lon": 38.7936719},
        "ne": {"lat": 37.380932, "lon": 48.8412702},
    },
    "ISL": {
        "sw": {"lat": 63.0859177, "lon": -25.0135069},
        "ne": {"lat": 67.353, "lon": -12.8046162},
    },
    "ISR": {
        "sw": {"lat": 29.4533796, "lon": 34.2674994},
        "ne": {"lat": 33.3356317, "lon": 35.8950234},
    },
    "ITA": {
        "sw": {"lat": 35.2889616, "lon": 6.6272658},
        "ne": {"lat": 47.0921462, "lon": 18.7844746},
    },
    "JAM": {
        "sw": {"lat": 16.5899443, "lon": -78.5782366},
        "ne": {"lat": 18.7256394, "lon": -75.7541143},
    },
    "JEY": {
        "sw": {"lat": 49.1625179, "lon": -2.254512},
        "ne": {"lat": 49.2621288, "lon": -2.0104193},
    },
    "JOR": {
        "sw": {"lat": 29.183401, "lon": 34.8844372},
        "ne": {"lat": 33.3750617, "lon": 39.3012981},
    },
    "JPN": {
        "sw": {"lat": 20.2145811, "lon": 122.7141754},
        "ne": {"lat": 45.7112046, "lon": 154.205541},
    },
    "KAZ": {
        "sw": {"lat": 40.5686476, "lon": 46.4932179},
        "ne": {"lat": 55.4421701, "lon": 87.3156316},
    },
    "KEN": {
        "sw": {"lat": -4.8995204, "lon": 33.9098987},
        "ne": {"lat": 4.62, "lon": 41.899578},
    },
    "KGZ": {
        "sw": {"lat": 39.1728437, "lon": 69.2649523},
        "ne": {"lat": 43.2667971, "lon": 80.2295793},
    },
    "KHM": {
        "sw": {"lat": 9.4752639, "lon": 102.3338282},
        "ne": {"lat": 14.6904224, "lon": 107.6276788},
    },
    "KIR": {
        "sw": {"lat": -7.0516717, "lon": -179.1645388},
        "ne": {"lat": 7.9483283, "lon": -164.1645388},
    },
    "KNA": {
        "sw": {"lat": 16.895, "lon": -63.051129},
        "ne": {"lat": 17.6158146, "lon": -62.3303519},
    },
    "KOR": {
        "sw": {"lat": 32.9104556, "lon": 124.354847},
        "ne": {"lat": 38.623477, "lon": 132.1467806},
    },
    "KWT": {
        "sw": {"lat": 28.5243622, "lon": 46.5526837},
        "ne": {"lat": 30.1038082, "lon": 49.0046809},
    },
    "LAO": {
        "sw": {"lat": 13.9096752, "lon": 100.0843247},
        "ne": {"lat": 22.5086717, "lon": 107.6349989},
    },
    "LBN": {
        "sw": {"lat": 33.0479858, "lon": 34.8825667},
        "ne": {"lat": 34.6923543, "lon": 36.625},
    },
    "LBR": {
        "sw": {"lat": 4.1555907, "lon": -11.6080764},
        "ne": {"lat": 8.5519861, "lon": -7.367323},
    },
    "LBY": {
        "sw": {"lat": 19.5008138, "lon": 9.391081},
        "ne": {"lat": 33.3545898, "lon": 25.3770629},
    },
    "LCA": {
        "sw": {"lat": 13.508, "lon": -61.2853867},
        "ne": {"lat": 14.2725, "lon": -60.6669363},
    },
    "LIE": {
        "sw": {"lat": 47.0484291, "lon": 9.4716736},
        "ne": {"lat": 47.270581, "lon": 9.6357143},
    },
    "LKA": {
        "sw": {"lat": 5.719, "lon": 79.3959205},
        "ne": {"lat": 10.035, "lon": 82.0810141},
    },
    "LSO": {
        "sw": {"lat": -30.6772773, "lon": 27.0114632},
        "ne": {"lat": -28.570615, "lon": 29.4557099},
    },
    "LTU": {
        "sw": {"lat": 53.8967893, "lon": 20.653783},
        "ne": {"lat": 56.4504213, "lon": 26.8355198},
    },
    "LUX": {
        "sw": {"lat": 49.4969821, "lon": 4.9684415},
        "ne": {"lat": 50.430377, "lon": 6.0344254},
    },
    "LVA": {
        "sw": {"lat": 55.6746505, "lon": 20.6715407},
        "ne": {"lat": 58.0855688, "lon": 28.2414904},
    },
    "MAC": {
        "sw": {"lat": 22.0766667, "lon": 113.5281666},
        "ne": {"lat": 22.2170361, "lon": 113.6301389},
    },
    "MAF": {
        "sw": {"lat": 17.8963535, "lon": -63.3605643},
        "ne": {"lat": 18.1902778, "lon": -62.7644063},
    },
    "MAR": {
        "sw": {"lat": 21.3365321, "lon": -17.2551456},
        "ne": {"lat": 36.0505269, "lon": -0.998429},
    },
    "MCO": {
        "sw": {"lat": 43.7247599, "lon": 7.4090279},
        "ne": {"lat": 43.7519311, "lon": 7.4398704},
    },
    "MDA": {
        "sw": {"lat": 45.4674139, "lon": 26.6162189},
        "ne": {"lat": 48.4918695, "lon": 30.1636756},
    },
    "MDG": {
        "sw": {"lat": -25.6071002, "lon": 43.2202072},
        "ne": {"lat": -11.9519693, "lon": 50.4862553},
    },
    "MDV": {
        "sw": {"lat": -0.9074935, "lon": 72.3554187},
        "ne": {"lat": 7.3106246, "lon": 73.9700962},
    },
    "MEX": {
        "sw": {"lat": 14.3886243, "lon": -118.59919},
        "ne": {"lat": 32.7186553, "lon": -86.493266},
    },
    "MHL": {
        "sw": {"lat": -0.5481258, "lon": 163.4985095},
        "ne": {"lat": 14.4518742, "lon": 178.4985095},
    },
    "MKD": {
        "sw": {"lat": 40.8536596, "lon": 20.4529023},
        "ne": {"lat": 42.3735359, "lon": 23.034051},
    },
    "MLI": {
        "sw": {"lat": 10.147811, "lon": -12.2402835},
        "ne": {"lat": 25.001084, "lon": 4.2673828},
    },
    "MLT": {
        "sw": {"lat": 35.6029696, "lon": 13.9324226},
        "ne": {"lat": 36.2852706, "lon": 14.8267966},
    },
    "MMR": {
        "sw": {"lat": 9.4399432, "lon": 92.1719423},
        "ne": {"lat": 28.547835, "lon": 101.1700796},
    },
    "MNE": {
        "sw": {"lat": 41.7495999, "lon": 18.4195781},
        "ne": {"lat": 43.5585061, "lon": 20.3561641},
    },
    "MNG": {
        "sw": {"lat": 41.5800276, "lon": 87.73762},
        "ne": {"lat": 52.1496, "lon": 119.931949},
    },
    "MNP": {
        "sw": {"lat": 14.036565, "lon": 144.813338},
        "ne": {"lat": 20.616556, "lon": 146.154418},
    },
    "MOZ": {
        "sw": {"lat": -26.9209427, "lon": 30.2138197},
        "ne": {"lat": -10.3252149, "lon": 41.0545908},
    },
    "MRT": {
        "sw": {"lat": 14.7209909, "lon": -17.068081},
        "ne": {"lat": 27.314942, "lon": -4.8333344},
    },
    "MSR": {
        "sw": {"lat": 16.475, "lon": -62.450667},
        "ne": {"lat": 17.0152978, "lon": -61.9353818},
    },
    "MTQ": {
        "sw": {"lat": 14.3948596, "lon": -61.2290815},
        "ne": {"lat": 14.8787029, "lon": -60.8095833},
    },
    "MUS": {
        "sw": {"lat": -20.725, "lon": 56.3825151},
        "ne": {"lat": -10.138, "lon": 63.7151319},
    },
    "MWI": {
        "sw": {"lat": -17.1296031, "lon": 32.6703616},
        "ne": {"lat": -9.3683261, "lon": 35.9185731},
    },
    "MYS": {
        "sw": {"lat": -5.1076241, "lon": 105.3471939},
        "ne": {"lat": 9.8923759, "lon": 120.3471939},
    },
    "MYT": {
        "sw": {"lat": -13.0210119, "lon": 45.0183298},
        "ne": {"lat": -12.6365902, "lon": 45.2999917},
    },
    "NAM": {
        "sw": {"lat": -28.96945, "lon": 11.5280384},
        "ne": {"lat": -16.9634855, "lon": 25.2617671},
    },
    "NCL": {
        "sw": {"lat": -23.2217509, "lon": 162.6034343},
        "ne": {"lat": -17.6868616, "lon": 167.8109827},
    },
    "NER": {
        "sw": {"lat": 11.693756, "lon": 0.1689653},
        "ne": {"lat": 23.517178, "lon": 15.996667},
    },
    "NFK": {
        "sw": {"lat": -29.333, "lon": 167.6873878},
        "ne": {"lat": -28.796, "lon": 168.2249543},
    },
    "NGA": {
        "sw": {"lat": 4.0690959, "lon": 2.676932},
        "ne": {"lat": 13.885645, "lon": 14.678014},
    },
    "NIC": {
        "sw": {"lat": 10.7076565, "lon": -87.901532},
        "ne": {"lat": 15.0331183, "lon": -82.6227023},
    },
    "NIU": {
        "sw": {"lat": -19.3548665, "lon": -170.1595029},
        "ne": {"lat": -18.7534559, "lon": -169.5647229},
    },
    "NLD": {
        "sw": {"lat": 50.7295671, "lon": 1.9193492},
        "ne": {"lat": 53.7253321, "lon": 7.2274985},
    },
    "NOR": {
        "sw": {"lat": 57.7590052, "lon": 4.0875274},
        "ne": {"lat": 71.3848787, "lon": 31.7614911},
    },
    "NPL": {
        "sw": {"lat": 26.3477581, "lon": 80.0586226},
        "ne": {"lat": 30.446945, "lon": 88.2015257},
    },
    "NRU": {
        "sw": {"lat": -0.5541334, "lon": 166.9091794},
        "ne": {"lat": -0.5025906, "lon": 166.9589235},
    },
    "NZL": {
        "sw": {"lat": -52.8213687, "lon": -179.059153},
        "ne": {"lat": -29.0303303, "lon": 179.3643594},
    },
    "OMN": {
        "sw": {"lat": 16.4649608, "lon": 52},
        "ne": {"lat": 26.7026737, "lon": 60.054577},
    },
    "PAK": {
        "sw": {"lat": 23.5393916, "lon": 60.872855},
        "ne": {"lat": 37.084107, "lon": 77.1203914},
    },
    "PAN": {
        "sw": {"lat": 7.0338679, "lon": -83.0517245},
        "ne": {"lat": 9.8701757, "lon": -77.1393779},
    },
    "PCN": {
        "sw": {"lat": -25.1306736, "lon": -130.8049862},
        "ne": {"lat": -23.8655769, "lon": -124.717534},
    },
    "PER": {
        "sw": {"lat": -20.1984472, "lon": -84.6356535},
        "ne": {"lat": -0.0392818, "lon": -68.6519906},
    },
    "PHL": {
        "sw": {"lat": 4.2158064, "lon": 114.0952145},
        "ne": {"lat": 21.3217806, "lon": 126.8072562},
    },
    "PLW": {
        "sw": {"lat": 2.748, "lon": 131.0685462},
        "ne": {"lat": 8.222, "lon": 134.7714735},
    },
    "PNG": {
        "sw": {"lat": -13.1816069, "lon": 136.7489081},
        "ne": {"lat": 1.8183931, "lon": 151.7489081},
    },
    "POL": {
        "sw": {"lat": 49.0020468, "lon": 14.1229707},
        "ne": {"lat": 55.0336963, "lon": 24.145783},
    },
    "PRI": {
        "sw": {"lat": 17.9268695, "lon": -67.271492},
        "ne": {"lat": 18.5159789, "lon": -65.5897525},
    },
    "PRK": {
        "sw": {"lat": 37.5867855, "lon": 124.0913902},
        "ne": {"lat": 43.0089642, "lon": 130.924647},
    },
    "PRT": {
        "sw": {"lat": 29.8288021, "lon": -31.5575303},
        "ne": {"lat": 42.1543112, "lon": -6.1891593},
    },
    "PRY": {
        "sw": {"lat": -27.6063935, "lon": -62.6442036},
        "ne": {"lat": -19.2876472, "lon": -54.258},
    },
    "PSE": {
        "sw": {"lat": 31.2201289, "lon": 34.0689732},
        "ne": {"lat": 32.5521479, "lon": 35.5739235},
    },
    "PYF": {
        "sw": {"lat": -28.0990232, "lon": -154.9360599},
        "ne": {"lat": -7.6592173, "lon": -134.244799},
    },
    "QAT": {
        "sw": {"lat": 24.4707534, "lon": 50.5675},
        "ne": {"lat": 26.3830212, "lon": 52.638011},
    },
    "REU": {
        "sw": {"lat": -21.3897308, "lon": 55.2164268},
        "ne": {"lat": -20.8717136, "lon": 55.8366924},
    },
    "ROU": {
        "sw": {"lat": 43.618682, "lon": 20.2619773},
        "ne": {"lat": 48.2653964, "lon": 30.0454257},
    },
    "RUS": {
        "sw": {"lat": 41.1850968, "lon": 19.6389},
        "ne": {"lat": 82.0586232, "lon": 180},
    },
    "RWA": {
        "sw": {"lat": -2.8389804, "lon": 28.8617546},
        "ne": {"lat": -1.0474083, "lon": 30.8990738},
    },
    "SAU": {
        "sw": {"lat": 16.29, "lon": 34.4571718},
        "ne": {"lat": 32.1543377, "lon": 55.6666851},
    },
    "SDN": {
        "sw": {"lat": 8.685278, "lon": 21.8145046},
        "ne": {"lat": 22.224918, "lon": 39.0576252},
    },
    "SEN": {
        "sw": {"lat": 12.2372838, "lon": -17.7862419},
        "ne": {"lat": 16.6919712, "lon": -11.3458996},
    },
    "SGP": {
        "sw": {"lat": 1.1304753, "lon": 103.6920359},
        "ne": {"lat": 1.4504753, "lon": 104.0120359},
    },
    "SGS": {
        "sw": {"lat": -59.684, "lon": -42.354739},
        "ne": {"lat": -53.3500755, "lon": -25.8468303},
    },
    "SHN": {
        "sw": {"lat": -16.23, "lon": -5.9973424},
        "ne": {"lat": -15.704, "lon": -5.4234153},
    },
    "SJM": {
        "sw": {"lat": 70.6260825, "lon": -9.6848146},
        "ne": {"lat": 81.028076, "lon": 34.6891253},
    },
    "SLB": {
        "sw": {"lat": -13.2424298, "lon": 155.3190556},
        "ne": {"lat": -4.81085, "lon": 170.3964667},
    },
    "SLE": {
        "sw": {"lat": 6.755, "lon": -13.5003389},
        "ne": {"lat": 9.999973, "lon": -10.271683},
    },
    "SLV": {
        "sw": {"lat": 12.976046, "lon": -90.1790975},
        "ne": {"lat": 14.4510488, "lon": -87.6351394},
    },
    "SMR": {
        "sw": {"lat": 43.8937002, "lon": 12.4033246},
        "ne": {"lat": 43.992093, "lon": 12.5160665},
    },
    "SOM": {
        "sw": {"lat": -1.8031969, "lon": 40.98918},
        "ne": {"lat": 12.1889121, "lon": 51.6177696},
    },
    "SPM": {
        "sw": {"lat": 46.5507173, "lon": -56.6972961},
        "ne": {"lat": 47.365, "lon": -55.9033333},
    },
    "SRB": {
        "sw": {"lat": 42.2322435, "lon": 18.8142875},
        "ne": {"lat": 46.1900524, "lon": 23.006309},
    },
    "STP": {
        "sw": {"lat": -0.2135137, "lon": 6.260642},
        "ne": {"lat": 1.9257601, "lon": 7.6704783},
    },
    "SUR": {
        "sw": {"lat": 1.8312802, "lon": -58.070833},
        "ne": {"lat": 6.225, "lon": -53.8433358},
    },
    "SVK": {
        "sw": {"lat": 47.7314286, "lon": 16.8331891},
        "ne": {"lat": 49.6138162, "lon": 22.56571},
    },
    "SVN": {
        "sw": {"lat": 45.4214242, "lon": 13.3754696},
        "ne": {"lat": 46.8766816, "lon": 16.5967702},
    },
    "SWE": {
        "sw": {"lat": 55.1331192, "lon": 10.5930952},
        "ne": {"lat": 69.0599699, "lon": 24.1776819},
    },
    "SWZ": {
        "sw": {"lat": -27.3175201, "lon": 30.7908},
        "ne": {"lat": -25.71876, "lon": 32.1349923},
    },
    "SYC": {
        "sw": {"lat": -10.4649258, "lon": 45.9988759},
        "ne": {"lat": -3.512, "lon": 56.4979396},
    },
    "SYR": {
        "sw": {"lat": 32.311354, "lon": 35.4714427},
        "ne": {"lat": 37.3184589, "lon": 42.3745687},
    },
    "TCA": {
        "sw": {"lat": 20.9553418, "lon": -72.6799046},
        "ne": {"lat": 22.1630989, "lon": -70.8643591},
    },
    "TCD": {
        "sw": {"lat": 7.44107, "lon": 13.47348},
        "ne": {"lat": 23.4975, "lon": 24.0},
    },
    "TGO": {
        "sw": {"lat": 5.926547, "lon": -0.1439746},
        "ne": {"lat": 11.1395102, "lon": 1.8087605},
    },
    "THA": {
        "sw": {"lat": 5.612851, "lon": 97.3438072},
        "ne": {"lat": 20.4648337, "lon": 105.636812},
    },
    "TJK": {
        "sw": {"lat": 36.6711153, "lon": 67.3332775},
        "ne": {"lat": 41.0450935, "lon": 75.1539563},
    },
    "TKL": {
        "sw": {"lat": -9.6442499, "lon": -172.7213673},
        "ne": {"lat": -8.3328631, "lon": -170.9797586},
    },
    "TKM": {
        "sw": {"lat": 35.129093, "lon": 52.335076},
        "ne": {"lat": 42.7975571, "lon": 66.6895177},
    },
    "TLS": {
        "sw": {"lat": -9.5642775, "lon": 124.0415703},
        "ne": {"lat": -8.0895459, "lon": 127.5335392},
    },
    "TON": {
        "sw": {"lat": -24.1034499, "lon": -179.3866055},
        "ne": {"lat": -15.3655722, "lon": -173.5295458},
    },
    "TTO": {
        "sw": {"lat": 9.8732106, "lon": -62.083056},
        "ne": {"lat": 11.5628372, "lon": -60.2895848},
    },
    "TUN": {
        "sw": {"lat": 30.230236, "lon": 7.5219807},
        "ne": {"lat": 37.7612052, "lon": 11.8801133},
    },
    "TUR": {
        "sw": {"lat": 35.8076804, "lon": 25.6212891},
        "ne": {"lat": 42.297, "lon": 44.8176638},
    },
    "TUV": {
        "sw": {"lat": -9.9939389, "lon": 175.1590468},
        "ne": {"lat": -5.4369611, "lon": 178.7344938},
    },
    "TWN": {
        "sw": {"lat": 10.374269, "lon": 114.3599058},
        "ne": {"lat": 26.4372222, "lon": 122.297},
    },
    "TZA": {
        "sw": {"lat": -11.761254, "lon": 29.3269773},
        "ne": {"lat": -0.9854812, "lon": 40.6584071},
    },
    "UGA": {
        "sw": {"lat": -1.4823179, "lon": 29.573433},
        "ne": {"lat": 4.2340766, "lon": 35.000308},
    },
    "UKR": {
        "sw": {"lat": 44.184598, "lon": 22.137059},
        "ne": {"lat": 52.3791473, "lon": 40.2275801},
    },
    "UMI": {
        "sw": {"lat": 6.1779744, "lon": -162.6816297},
        "ne": {"lat": 6.6514388, "lon": -162.1339885},
    },
    "URY": {
        "sw": {"lat": -35.7824481, "lon": -58.4948438},
        "ne": {"lat": -30.0853962, "lon": -53.0755833},
    },
    "USA": {
        "sw": {"lat": 24.9493, "lon": -125.0011},
        "ne": {"lat": 49.5904, "lon": -66.9326},
    },
    "UZB": {
        "sw": {"lat": 37.1821164, "lon": 55.9977865},
        "ne": {"lat": 45.590118, "lon": 73.1397362},
    },
    "VAT": {
        "sw": {"lat": 41.9002044, "lon": 12.4457442},
        "ne": {"lat": 41.9073912, "lon": 12.4583653},
    },
    "VCT": {
        "sw": {"lat": 12.5166548, "lon": -61.6657471},
        "ne": {"lat": 13.583, "lon": -60.9094146},
    },
    "VEN": {
        "sw": {"lat": 0.647529, "lon": -73.3529632},
        "ne": {"lat": 15.9158431, "lon": -59.5427079},
    },
    "VGB": {
        "sw": {"lat": 17.623468, "lon": -65.159094},
        "ne": {"lat": 18.464984, "lon": -64.512674},
    },
    "VIR": {
        "sw": {"lat": 17.623468, "lon": -65.159094},
        "ne": {"lat": 18.464984, "lon": -64.512674},
    },
    "VNM": {
        "sw": {"lat": 8.1790665, "lon": 102.14441},
        "ne": {"lat": 23.393395, "lon": 114.3337595},
    },
    "VUT": {
        "sw": {"lat": -20.4627425, "lon": 166.3355255},
        "ne": {"lat": -12.8713777, "lon": 170.449982},
    },
    "WLF": {
        "sw": {"lat": -14.5630748, "lon": -178.3873749},
        "ne": {"lat": -12.9827961, "lon": -175.9190391},
    },
    "WSM": {
        "sw": {"lat": -14.2770916, "lon": -173.0091864},
        "ne": {"lat": -13.2381892, "lon": -171.1929229},
    },
    "YEM": {
        "sw": {"lat": 11.9084802, "lon": 41.60825},
        "ne": {"lat": 19.0, "lon": 54.7389375},
    },
    "ZAF": {
        "sw": {"lat": -47.1788335, "lon": 16.3335213},
        "ne": {"lat": -22.1250301, "lon": 38.2898954},
    },
    "ZMB": {
        "sw": {"lat": -18.0765945, "lon": 21.9993509},
        "ne": {"lat": -8.2712822, "lon": 33.701111},
    },
    "ZWE": {
        "sw": {"lat": -22.4241096, "lon": 25.2373},
        "ne": {"lat": -15.6097033, "lon": 33.0683413},
    },
}