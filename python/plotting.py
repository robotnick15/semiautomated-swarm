from graph import Graph
from views import draw2
import numpy as np
from shapely.geometry.point import Point

# Copy params from simulations here
dims = np.array([(-500, 2500), (-100, 2900), (-50, -50)])
# obstacles = [(Point(1250, 1000).buffer(200)), 
#                 (Point(1500, 1500).buffer(200)),
#                 (Point(750, 1250).buffer(200)),
#                 (Point(800, 650).buffer(200)),
#                 (Point(1500, 500).buffer(200)),
#                 (Point(1800, 1000).buffer(200)),
#                 (Point(2000, 1400).buffer(200)),
#                 (Point(1200, 1800).buffer(200))]
obstacles = [Point(2000, 1400).buffer(1200)]      
graph = Graph(dims, obstacles)
init = (100.0, 100.0, -50)
goal = (2300.0, 2600.0, -50.0)


# trails printed at the end of simulation

trail = [[(381.35742890545976, 50.00549244343806, -50), (440.98923382485145, 92.46514469224296, -50.0), (457.5294727343865, 137.64123137678388, -50.0), (483.8770437369818, 204.68590953772463, -50.0), (529.137208557601, 292.5503985596922, -50.0), (565.8478871425897, 351.75730060707855, -50.0), (586.6665579782364, 392.61475437756803, -50.0)], [(440.98923382485145, 92.46514469224296, -50.0), (459.09419630431535, 108.50918431013456, -50.0), (531.8676482187943, 171.7273785249718, -50.0), (594.5639565782858, 234.7642673177579, -50.0), (633.2208236821467, 275.60350096009086, -50.0), (670.5974718775299, 324.311450438624, -50.0), (707.4992412093661, 388.0387238558066, -50.0)], [(459.09419630431535, 108.50918431013456, -50.0), (510.44330479554185, 159.8039515455477, -50.0), (568.9174190650269, 231.16768594856526, -50.0), (612.636011918857, 283.23067811664396, -50.0), (665.9073727358978, 356.0446316115867, -50.0), (715.3730928062621, 408.6567414132138, -50.0)], [(510.44330479554185, 159.8039515455477, -50.0), (560.997850435065, 238.82885608087184, -50.0), (615.8515326243516, 318.7040244292829, -50.0), (634.4425284743726, 343.15913381297173, -50.0), (692.5075004943452, 413.58686576772186, -50.0), (730.9514672741404, 489.19634891522816, -50.0)], [(560.997850435065, 238.82885608087184, -50.0), (605.0148252992882, 328.62031404766475, -50.0), (628.5890602692909, 384.1479455810881, -50.0), (667.5200175494783, 464.8950671742158, -50.0), (698.8966002731299, 503.21775853008876, -50.0), (734.2679151897545, 595.0752058712676, -50.0)], [(605.0148252992882, 328.62031404766475, -50.0), (610.3438381028404, 404.4049596728271, -50.0), (615.18149001372, 497.9950589643572, -50.0), (636.0712359274903, 570.8179415384362, -50.0), (649.1589626785601, 642.8658156403646, -50.0), (662.0445344561886, 709.3068814487049, -50.0)], [(610.3438381028404, 404.4049596728271, -50.0), (623.5186154724665, 463.9851686294306, -50.0), (623.1960003362917, 560.7262937805901, -50.0), (632.1931993643041, 620.894205505168, -50.0), (650.2169799700512, 713.8525978722082, -50.0), (671.660255022396, 787.2365352965409, -50.0)], [(623.5186154724665, 463.9851686294306, -50.0), (668.0653261127303, 553.5149992510319, -50.0), (679.3752764455686, 577.1173110514521, -50.0), (715.3984760414619, 668.7143333092416, -50.0), (742.0982102232285, 749.5460515856353, -50.0), (747.3799945431125, 833.672046974586, -50.0)], [(668.0653261127303, 553.5149992510319, -50.0), (700.8971185661242, 618.8003134019494, -50.0), (725.0620135315385, 677.8000980429015, -50.0), (746.5967137991546, 761.9693175623165, -50.0), (757.4845429862537, 834.7758521573589, -50.0), (753.6099924268583, 907.2052551893153, -50.0)], [(700.8971185661242, 618.8003134019494, -50.0), (704.5131747891926, 672.3718129376751, -50.0), (708.9649761643981, 754.8421900449887, -50.0), (720.8628136090739, 842.5900227500872, -50.0), (725.3645513477745, 935.8930158687128, -50.0), (727.8672258679679, 1003.8922325851704, -50.0)], [(704.5131747891926, 672.3718129376751, -50.0), (705.6638126904137, 684.4648556809726, -50.0), (723.1465590231114, 778.3697092760923, -50.0), (731.0785418637099, 864.1412462459766, -50.0), (744.8437965905073, 963.1540999595918, -50.0), (746.3157736489147, 1062.468570220242, -50.0)], [(705.6638126904137, 684.4648556809726, -50.0), (719.7335728543717, 783.4701174044219, -50.0), (720.8465113070858, 879.3273435983442, -50.0), (732.8286971978664, 972.0091124726537, -50.0), (733.8991376783233, 1002.3313953963332, -50.0), (742.6696803278976, 1067.0314861888091, -50.0)], [(719.7335728543717, 783.4701174044219, -50.0), (723.3580690707684, 816.0961808292791, -50.0), (731.079111781838, 897.586559161633, -50.0), (733.854765666111, 986.3981871383795, -50.0), (739.3252302764729, 1017.9087291698334, -50.0), (745.2937934994336, 1092.0678091454058, -50.0), (746.0653545458268, 1180.0563393030966, -50.0)], [(723.3580690707684, 816.0961808292791, -50.0), (728.1200259121154, 854.2625237093031, -50.0), (749.8594970924942, 946.609672495767, -50.0), (760.8999154912267, 983.6280436448293, -50.0), (755.3701179799707, 1063.4176474831622, -50.0), (772.6986148931331, 1160.575968629965, -50.0), (773.3853157700946, 1208.178603979223, -50.0)], [(728.1200259121154, 854.2625237093031, -50.0), (732.7451277077848, 888.2208532713813, -50.0), (741.9271518654888, 968.6296934893314, -50.0), (754.5874948758648, 1066.2645195908385, -50.0), (759.4582402008858, 1105.4025167860837, -50.0), (759.815688656697, 1128.5845101718144, -50.0), (749.4921097270656, 1224.867954022061, -50.0)], [(732.7451277077848, 888.2208532713813, -50.0), (742.7904181821534, 962.4728747087644, -50.0), (752.9280477245122, 1040.2211737755727, -50.0), (759.7552573676909, 1135.16744325963, -50.0), (760.0510102385081, 1176.795817167233, -50.0), (761.7429951065916, 1270.9378975438394, -50.0)], [(742.7904181821534, 962.4728747087644, -50.0), (751.0658732280048, 1058.8648348841514, -50.0), (758.0122577031294, 1152.0326301093235, -50.0), (765.7935233104155, 1246.9817931483199, -50.0), (773.6185351035109, 1288.0287403899388, -50.0), (779.239495864095, 1332.8922724123638, -50.0)], [(751.0658732280048, 1058.8648348841514, -50.0), (753.346984864344, 1114.8065922257126, -50.0), (756.7717901943417, 1163.8133774058886, -50.0), (762.5324268390002, 1242.3343305559183, -50.0), (770.4281684742313, 1307.6801537707943, -50.0), (778.9861379637358, 1407.1479804244495, -50.0), (774.3580404712144, 1455.6986829852171, -50.0)], [(753.346984864344, 1114.8065922257126, -50.0), (767.9173493302519, 1200.9622355684478, -50.0), (766.9830268163795, 1287.8415671126074, -50.0), (771.9506453743395, 1320.3493842746254, -50.0), (783.2878654051028, 1413.020101885404, -50.0), (795.2927324192052, 1497.7932818306292, -50.0)], [(767.9173493302519, 1200.9622355684478, -50.0), (767.8626882338507, 1266.220458378032, -50.0), (764.7951434193021, 1349.5271112343735, -50.0), (775.572496382038, 1442.4570549051964, -50.0), (779.3468297317831, 1534.533447567189, -50.0), (779.7000578762262, 1543.6996180831673, -50.0), (785.7372350144059, 1589.9840812285406, -50.0)], [(767.8626882338507, 1266.220458378032, -50.0), (775.5715133058053, 1334.7470887846703, -50.0), (788.4570394905771, 1408.072624308508, -50.0), (796.3099823115405, 1455.7170958777397, -50.0), (804.8794980049439, 1543.2415901895022, -50.0), (820.6494109923145, 1630.7159995708444, -50.0)], [(775.5715133058053, 1334.7470887846703, -50.0), (784.7372188049206, 1419.2260915347233, -50.0), (793.208325160442, 1492.1434555335593, -50.0), (805.1624932036098, 1547.6980413051779, -50.0), (819.29802435013, 1612.6351556655954, -50.0), (830.7276673917906, 1681.274051387206, -50.0), (843.1617046208693, 1722.7027885332627, -50.0)], [(784.7372188049206, 1419.2260915347233, -50.0), (787.9891962346223, 1449.2197601147989, -50.0), (799.8303304411032, 1532.7446173403073, -50.0), (808.2243827264471, 1584.5944404698253, -50.0), (817.2145882345841, 1646.613461657179, -50.0), (837.0404959710961, 1713.3791733690034, -50.0), (864.3225501562333, 1801.6495167815447, -50.0)], [(787.9891962346223, 1449.2197601147989, -50.0), (802.1381546117831, 1538.0422742284159, -50.0), (817.7324139764953, 1622.1190668378317, -50.0), (836.5684325981154, 1713.5281091762047, -50.0), (842.8522904252824, 1751.7858095640818, -50.0), (870.8580408091609, 1831.499045399934, -50.0)], [(802.1381546117831, 1538.0422742284159, -50.0), (809.6362284304288, 1596.5334397993074, -50.0), (820.4491205847326, 1636.7471805583675, -50.0), (834.1359212859686, 1728.6784263702273, -50.0), (843.733885871279, 1797.6316331810353, -50.0), (878.4595291597859, 1856.4242127914933, -50.0), (911.8911312575525, 1914.2159067988596, -50.0)], [(809.6362284304288, 1596.5334397993074, -50.0), (827.3289451793233, 1667.5314895939678, -50.0), (841.262678350103, 1728.5173180718052, -50.0), (862.1363894921258, 1800.6260944585292, -50.0), (869.5240541308053, 1824.689241237954, -50.0), (904.7086162943546, 1905.9945313630192, -50.0), (920.4786972245897, 1945.3688667348456, -50.0)], [(827.3289451793233, 1667.5314895939678, -50.0), (837.6788329593122, 1708.483597198518, -50.0), (853.9929563657341, 1777.9092141261922, -50.0), (869.0810284461618, 1846.5396584931873, -50.0), (887.4293982135513, 1895.6986616783395, -50.0), (921.9714558967244, 1969.0373920505617, -50.0), (959.6219110948686, 2038.972984783934, -50.0)], [(837.6788329593122, 1708.483597198518, -50.0), (852.0157451576838, 1753.3154659339386, -50.0), (876.6272886995025, 1836.391626073951, -50.0), (915.5332686815442, 1917.2401587452284, -50.0), (951.4331143753535, 1984.0230855106504, -50.0), (977.0460284729702, 2054.277842572354, -50.0)], [(852.0157451576838, 1753.3154659339386, -50.0), (858.424254327303, 1805.292227317879, -50.0), (879.2985109058241, 1863.2700990645176, -50.0), (887.0977575117716, 1908.6472908360458, -50.0), (931.8449390946272, 1978.085602810779, -50.0), (980.7098049594472, 2053.3450026852197, -50.0), (1024.5976883056378, 2109.48026679184, -50.0)], [(858.424254327303, 1805.292227317879, -50.0), (887.5020285837957, 1889.6458200225495, -50.0), (924.0767213730636, 1972.6167130240103, -50.0), (953.9535521876086, 2025.6365771499552, -50.0), (984.5305991244353, 2083.8973078723916, -50.0), (1035.5593445335967, 2161.9469006210225, -50.0)], [(887.5020285837957, 1889.6458200225495, -50.0), (919.7471963284967, 1937.586865098059, -50.0), (961.7978944155644, 2013.329517606656, -50.0), (1013.6660941516701, 2084.4234843784793, -50.0), (1052.6212687832024, 2156.8299487220756, -50.0), (1099.1663216453146, 2200.0473187686475, -50.0)], [(919.7471963284967, 1937.586865098059, -50.0), (936.7156040558767, 1964.9912045985805, -50.0), (985.6720313927908, 2048.3356399946865, -50.0), (1022.1137181574086, 2106.778609877289, -50.0), (1071.0673164453738, 2181.074377606924, -50.0), (1129.6504988856502, 2243.374714086783, -50.0), (1140.70837248083, 2258.7246751113967, -50.0)], [(936.7156040558767, 1964.9912045985805, -50.0), (971.8957287366479, 2027.0312326425505, -50.0), (1024.5054070643087, 2107.1537005341493, -50.0), (1066.3512826186193, 2168.172292422225, -50.0), (1121.9683234339789, 2247.4731174067224, -50.0), (1152.4226196810548, 2292.9992071255747, -50.0)], [(971.8957287366479, 2027.0312326425505, -50.0), (1017.6053063861455, 2103.527894971242, -50.0), (1068.0652758992521, 2163.194659923001, -50.0), (1112.5376135544766, 2208.651443072308, -50.0), (1163.1457950547933, 2265.7955486874944, -50.0), (1218.3602212440114, 2324.3632207872656, -50.0)], [(1017.6053063861455, 2103.527894971242, -50.0), (1058.9105326158858, 2155.326881022933, -50.0), (1103.5745597781065, 2212.3574667279727, -50.0), (1155.6851463263033, 2259.8277843364945, -50.0), (1215.1939272962386, 2310.299632132088, -50.0), (1287.6818678172708, 2376.178943099478, -50.0)], [(1058.9105326158858, 2155.326881022933, -50.0), (1116.0922756921132, 2213.2259441381343, -50.0), (1175.2564413546163, 2272.881324739848, -50.0), (1213.3857988148902, 2308.6908988623527, -50.0), (1263.337099446525, 2357.0857372268956, -50.0), (1311.9844080515359, 2396.5269751313213, -50.0), (1344.3889330823436, 2423.433836498476, -50.0)], [(1116.0922756921132, 2213.2259441381343, -50.0), (1143.0332776710018, 2248.9436424559017, -50.0), (1210.153781431853, 2311.6366525225394, -50.0), (1283.3852565709647, 2372.3372774178656, -50.0), (1359.365317952577, 2429.954528424989, -50.0), (1413.077710857691, 2464.0254510920713, -50.0)], [(1143.0332776710018, 2248.9436424559017, -50.0), (1182.939652465589, 2282.9542102053465, -50.0), (1251.4561082621917, 2341.492547030322, -50.0), (1314.7380249139655, 2395.4034085002645, -50.0), (1376.0191839243907, 2432.790068663012, -50.0), (1462.6757580201192, 2476.8519070538105, -50.0)], [(1182.939652465589, 2282.9542102053465, -50.0), (1254.2940444663645, 2346.989592578444, -50.0), (1327.7543682061166, 2400.6077679001296, -50.0), (1409.7847228468052, 2446.289531080365, -50.0), (1436.5695370913058, 2474.721086072027, -50.0), (1498.6421474188082, 2504.176241045253, -50.0)], [(1254.2940444663645, 2346.989592578444, -50.0), (1278.9587040452757, 2367.5064266882778, -50.0), (1346.5776341108951, 2424.387654282118, -50.0), (1395.5593679270823, 2461.7263933845534, -50.0), (1456.846354452655, 2503.946778208707, -50.0), (1528.4086684618833, 2541.4849737336785, -50.0), (1580.967274069337, 2562.9854218670057, -50.0)], [(1278.9587040452757, 2367.5064266882778, -50.0), (1363.8306237779236, 2419.4812539321038, -50.0), (1436.5860654727467, 2467.904382617142, -50.0), (1462.6585914569655, 2483.6553110396635, -50.0), (1547.2160180919923, 2527.577756806971, -50.0), (1615.8175238773306, 2567.2570399421365, -50.0)], [(1363.8306237779236, 2419.4812539321038, -50.0), (1389.8817647589117, 2437.5186868941164, -50.0), (1473.217415010294, 2485.873681726731, -50.0), (1531.6813201529803, 2517.0616329277054, -50.0), (1614.4606079706066, 2556.482499409521, -50.0), (1706.5753652209683, 2583.5321669451746, -50.0), (1721.5245821301667, 2596.915209579635, -50.0)], [(1389.8817647589117, 2437.5186868941164, -50.0), (1448.7942634196659, 2473.155304979809, -50.0), (1495.8178324404337, 2497.934908530063, -50.0), (1580.0742537000815, 2548.1783442581595, -50.0), (1671.187786658932, 2584.8626938088555, -50.0), (1731.1337235478243, 2607.5497047776057, -50.0)], [(1448.7942634196659, 2473.155304979809, -50.0), (1486.1750649690212, 2490.4124629751705, -50.0), (1577.2155502570738, 2525.6602954685436, -50.0), (1631.9254479810263, 2546.7638146918403, -50.0), (1671.9710412186976, 2559.6855637445565, -50.0), (1741.5391144741304, 2590.849712591897, -50.0), (1817.3872072941522, 2617.9843131862544, -50.0)], [(1486.1750649690212, 2490.4124629751705, -50.0), (1579.9213833450224, 2525.220907222873, -50.0), (1656.1120091518574, 2553.975128901781, -50.0), (1747.347634516785, 2581.9066684736226, -50.0), (1841.7993891063238, 2594.0018864160616, -50.0), (1862.6333423851725, 2598.5211024314594, -50.0)], [(1579.9213833450224, 2525.220907222873, -50.0), (1665.4510351944755, 2555.31752871064, -50.0), (1752.3977960164696, 2585.2593822073372, -50.0), (1812.432571479827, 2603.2686661672305, -50.0), (1859.7317344366902, 2617.9261505698278, -50.0), (1939.1686675118635, 2648.6481628558067, -50.0), (1957.699478372559, 2656.5282242918042, -50.0)], [(1665.4510351944755, 2555.31752871064, -50.0), (1728.794356662431, 2571.58537663975, -50.0), (1797.9755234197098, 2591.9719502644157, -50.0), (1881.0808224727584, 2618.081778604979, -50.0), (1958.287429793137, 2630.0936295236233, -50.0), (2050.117765374536, 2650.1194186315474, -50.0)], [(1728.794356662431, 2571.58537663975, -50.0), (1803.6869308887747, 2583.208190259306, -50.0), (1863.305463426742, 2595.0060994229666, -50.0), (1952.682877212797, 2600.9881163757404, -50.0), (2046.6108979128317, 2600.0039950853716, -50.0), (2126.9391302244144, 2594.0373639520712, -50.0)], [(1803.6869308887747, 2583.208190259306, -50.0), (1885.3846467154378, 2602.170449002006, -50.0), (1983.6519697990802, 2602.1651410747404, -50.0), (2060.9136322610957, 2604.468296586939, -50.0), (2128.8957246047244, 2601.6577012683083, -50.0), (2200.624754910962, 2599.164311869664, -50.0), (2300.0, 2600.0, -50.0)]]

# trail1 = [[(213.18060464640865, 19.577914156006635, -50), (269.46206768271986, 60.64301332593817, -50.0), (302.728576817427, 83.9041268971205, -50.0), (366.6649149402306, 118.07763014244463, -50.0), (410.20462633037494, 154.4624766962189, -50.0), (473.402705185023, 187.0301738285404, -50.0), (554.8724166427464, 221.68054631604244, -50.0)], [(269.46206768271986, 60.64301332593817, -50.0), (294.7966682724218, 99.32894030873618, -50.0), (327.25573247099356, 156.79905788463995, -50.0), (362.1622820960996, 226.51951125405782, -50.0), (393.6302737047988, 316.79899493358056, -50.0), (397.30630271535244, 323.77374641985085, -50.0), (428.0130644732834, 410.77643589088484, -50.0)], [(294.7966682724218, 99.32894030873618, -50.0), (308.0277254207805, 138.1728767418997, -50.0), (334.05535435361185, 198.35849288722966, -50.0), (350.3950383459262, 246.58546537438065, -50.0), (389.76471781572536, 337.2688083906078, -50.0), (429.87660745600476, 405.1797614668608, -50.0), (453.3917678597062, 462.9257163500663, -50.0)], [(308.0277254207805, 138.1728767418997, -50.0), (333.2078270736416, 200.61703622103136, -50.0), (384.36799504051265, 281.4907625810488, -50.0), (417.9652513440302, 358.36667588061994, -50.0), (449.8098421677132, 398.4780115277527, -50.0), (485.6105509868521, 484.08136977059223, -50.0)], [(333.2078270736416, 200.61703622103136, -50.0), (351.93743644574283, 237.07420823186908, -50.0), (396.4223646030431, 322.32197180127156, -50.0), (423.8481057026255, 397.4093918104595, -50.0), (438.0924078028562, 477.6250996622822, -50.0), (481.4768925296289, 565.1604589224381, -50.0)], [(351.93743644574283, 237.07420823186908, -50.0), (423.1191077344996, 302.3997690941402, -50.0), (463.81817769617237, 348.7332683790063, -50.0), (492.79641052438996, 406.39527319545783, -50.0), (523.3981548209811, 476.6978816922408, -50.0), (545.1058246738935, 548.1191021686082, -50.0), (547.5365950626198, 581.1639982431286, -50.0)], [(423.1191077344996, 302.3997690941402, -50.0), (480.95918403693577, 382.6067125889249, -50.0), (492.2361823651745, 445.8985383831956, -50.0), (495.0929760340044, 497.9728372320594, -50.0), (517.7215601108023, 559.8193890174024, -50.0), (555.5891861336906, 651.5193548025742, -50.0), (560.7198930427755, 666.7299188571899, -50.0)], [(480.95918403693577, 382.6067125889249, -50.0), (506.5874531502983, 470.3540656841874, -50.0), (521.5398364695853, 511.02393387210935, -50.0), (548.1669317853671, 594.6559076141039, -50.0), (556.7555231542926, 631.6695291501966, -50.0), (585.0314626566797, 722.5446827761236, -50.0), (605.3117301160936, 746.975269514069, -50.0)], [(506.5874531502983, 470.3540656841874, -50.0), (524.0151248984297, 515.7167082604064, -50.0), (567.0219846508203, 604.6892258073123, -50.0), (599.4608042416285, 697.9666165448735, -50.0), (620.8834646561064, 747.0099335136798, -50.0), (673.6467652616024, 811.6681669420698, -50.0)], [(524.0151248984297, 515.7167082604064, -50.0), (547.7310614872397, 588.1965398584775, -50.0), (564.6393631892539, 627.4077701588869, -50.0), (594.5128798408242, 687.4618231470475, -50.0), (620.3773505662014, 740.1598038558105, -50.0), (647.6576087181055, 789.9347191561251, -50.0), (668.5146102297186, 804.5985980270862, -50.0), (729.7796063135703, 850.5876271755303, -50.0)], [(547.7310614872397, 588.1965398584775, -50.0), (592.0317194715354, 677.2409002320571, -50.0), (631.5494318648801, 761.593692871267, -50.0), (673.674403504477, 814.0548969079507, -50.0), (727.1230182576746, 859.8839913402481, -50.0), (767.6926862384609, 896.7750899654837, -50.0)], [(592.0317194715354, 677.2409002320571, -50.0), (618.3448825444864, 742.1282919690126, -50.0), (668.6764767483651, 808.4090662708338, -50.0), (741.9337391203112, 869.3857290051116, -50.0), (815.2094717612495, 931.7890316640464, -50.0), (842.31831338971, 970.0579837424842, -50.0)], [(618.3448825444864, 742.1282919690126, -50.0), (659.1267169722557, 815.2003860120585, -50.0), (698.139132518462, 854.721361958946, -50.0), (759.4003887617669, 921.2976553854716, -50.0), (804.3467150146346, 966.9186578435042, -50.0), (868.3533522927876, 1026.5991549696857, -50.0), (880.2203792725126, 1041.4501661325219, -50.0)], [(659.1267169722557, 815.2003860120585, -50.0), (717.8324001120816, 874.583579075983, -50.0), (741.836787940288, 897.059825671826, -50.0), (798.2037491587771, 950.6683637944991, -50.0), (824.5680336972575, 965.1563445320726, -50.0), (905.0971878808816, 1024.2667201407237, -50.0), (958.4208912249155, 1061.3559970282606, -50.0)], [(717.8324001120816, 874.583579075983, -50.0), (767.5296878686414, 914.5635479574694, -50.0), (822.3994430361186, 959.9379265470986, -50.0), (891.6298003094771, 1015.7646415573134, -50.0), (942.1077275340604, 1055.421597857064, -50.0), (967.827000678403, 1079.1638063501891, -50.0), (1024.3477752323743, 1129.8958544778911, -50.0)], [(767.5296878686414, 914.5635479574694, -50.0), (808.293373143762, 957.7673365939447, -50.0), (846.3772754936098, 1001.0486194889234, -50.0), (893.9519621387866, 1055.0212346439578, -50.0), (923.0406980085262, 1089.6775442828043, -50.0), (984.1056201123185, 1160.5804917825897, -50.0), (1021.6299863213852, 1221.3472032194443, -50.0)], [(808.293373143762, 957.7673365939447, -50.0), (833.830196670575, 991.1853325884678, -50.0), (889.8227820049199, 1065.684376958652, -50.0), (947.9457460109379, 1130.3624579146808, -50.0), (1004.1735965108948, 1189.9357758324006, -50.0), (1053.180613023255, 1262.4964002091297, -50.0)], [(833.830196670575, 991.1853325884678, -50.0), (890.3223044190821, 1072.1533166912538, -50.0), (920.4664127496335, 1112.3046109009958, -50.0), (963.5796932736989, 1172.6283239615702, -50.0), (980.7175759211005, 1197.1945141905749, -50.0), (1029.7578202344391, 1261.1021181502283, -50.0), (1056.257282734273, 1292.2286875436935, -50.0)], [(890.3223044190821, 1072.1533166912538, -50.0), (930.7755898024653, 1117.0790962654964, -50.0), (995.2730216861316, 1189.3546673075423, -50.0), (1012.4505916407536, 1211.4477328516246, -50.0), (1074.2384200773326, 1284.4549604587228, -50.0), (1121.606823809247, 1349.0292008446522, -50.0), (1142.7995488632973, 1377.0330761124783, -50.0)], [(930.7755898024653, 1117.0790962654964, -50.0), (989.0058716465522, 1189.6320904535455, -50.0), (1009.174558585679, 1214.663089532327, -50.0), (1069.3857337846184, 1275.573904140787, -50.0), (1135.1063366478247, 1340.9949782084009, -50.0), (1183.6666102267916, 1407.4841056856426, -50.0)], [(989.0058716465522, 1189.6320904535455, -50.0), (1005.732745522844, 1229.4982376338937, -50.0), (1035.6545797649737, 1278.6535076634277, -50.0), (1075.6155660444774, 1330.4257314035663, -50.0), (1122.796761496002, 1390.4138774415178, -50.0), (1175.5060702246933, 1450.1870902616083, -50.0)], [(1005.732745522844, 1229.4982376338937, -50.0), (1079.074523548061, 1295.9199436424383, -50.0), (1129.1764989915391, 1363.6492669516379, -50.0), (1182.0542264633284, 1426.9476933503538, -50.0), (1210.4945748525556, 1468.8841096913218, -50.0), (1260.9834236827644, 1530.1034678119254, -50.0)], [(1079.074523548061, 1295.9199436424383, -50.0), (1100.9406975210484, 1336.8191135480806, -50.0), (1158.4489665604076, 1417.0076395397377, -50.0), (1205.3468692879321, 1472.1020652343325, -50.0), (1240.509253290418, 1525.5086449050173, -50.0), (1266.5189936536744, 1554.8322188676157, -50.0)], [(1100.9406975210484, 1336.8191135480806, -50.0), (1132.3699271260743, 1387.6541931025915, -50.0), (1188.6533206873567, 1457.6606317937385, -50.0), (1242.1519827999987, 1511.002238502145, -50.0), (1262.790739764111, 1535.3696026251773, -50.0), (1316.440272598604, 1596.8881191708304, -50.0), (1353.7212185898334, 1642.0743092624275, -50.0)], [(1132.3699271260743, 1387.6541931025915, -50.0), (1180.6212352191799, 1438.3030922961934, -50.0), (1205.0510413715617, 1470.9614289369847, -50.0), (1256.1509895934291, 1534.5036720651729, -50.0), (1295.9964231475133, 1580.4083120996547, -50.0), (1349.8784885245152, 1642.8668217732222, -50.0), (1389.1021419680917, 1687.8689590615534, -50.0)], [(1180.6212352191799, 1438.3030922961934, -50.0), (1217.8102040889235, 1483.183943662895, -50.0), (1273.8671264966488, 1549.2215847278972, -50.0), (1316.695489405483, 1602.182289296491, -50.0), (1380.3220738509476, 1664.455428966362, -50.0), (1458.346278781431, 1725.299749078728, -50.0)], [(1217.8102040889235, 1483.183943662895, -50.0), (1255.1913432856516, 1521.7676036336263, -50.0), (1300.7126988030866, 1579.2042195047343, -50.0), (1363.3380702395157, 1646.9888316728518, -50.0), (1430.9351754665424, 1717.1081179362031, -50.0), (1486.120905681602, 1778.578237310051, -50.0)], [(1255.1913432856516, 1521.7676036336263, -50.0), (1293.5139365622892, 1569.4896335498006, -50.0), (1348.6380294638188, 1636.2878596770695, -50.0), (1388.1272200641254, 1673.2853714433722, -50.0), (1441.610874731119, 1721.9701921028325, -50.0), (1466.64143093146, 1745.980105076951, -50.0), (1537.3095233641075, 1804.8566784732468, -50.0)], [(1293.5139365622892, 1569.4896335498006, -50.0), (1352.0318088739693, 1635.1650491656703, -50.0), (1417.169773081038, 1709.9560148640207, -50.0), (1466.241784639479, 1758.3444677661055, -50.0), (1494.9410251046215, 1792.8932595018784, -50.0), (1554.2753367678888, 1871.0801608183056, -50.0)], [(1352.0318088739693, 1635.1650491656703, -50.0), (1374.9310218464313, 1665.012492349012, -50.0), (1426.0625594205833, 1701.8671254591748, -50.0), (1492.4953087028919, 1764.868945951248, -50.0), (1536.9777687803542, 1820.0703325268616, -50.0), (1559.8720610025384, 1850.3241273520832, -50.0), (1626.7785251002647, 1906.521029471775, -50.0), (1635.4392977105636, 1916.012589017412, -50.0)], [(1374.9310218464313, 1665.012492349012, -50.0), (1440.9945232342675, 1740.0832175645005, -50.0), (1479.8492297508687, 1789.4509979617026, -50.0), (1539.6546379369695, 1864.3127812283951, -50.0), (1569.5696159129088, 1906.661506626882, -50.0), (1609.625059535096, 1987.655460510062, -50.0)], [(1440.9945232342675, 1740.0832175645005, -50.0), (1485.780314553995, 1829.4936917600098, -50.0), (1505.3440764668246, 1855.2144649000627, -50.0), (1572.6395660480803, 1928.465576394229, -50.0), (1621.509694363629, 1990.383294947898, -50.0), (1636.2543951103085, 2010.1936634933932, -50.0), (1679.9453453258666, 2057.4110574453584, -50.0)], [(1485.780314553995, 1829.4936917600098, -50.0), (1567.6014095646995, 1867.8881742744597, -50.0), (1628.567535216452, 1902.0105501910975, -50.0), (1697.8554185407074, 1946.4590601161906, -50.0), (1739.9566290623436, 1994.91213836363, -50.0), (1806.6773235768633, 2063.1543172262545, -50.0)], [(1567.6014095646995, 1867.8881742744597, -50.0), (1579.4667968301937, 1885.2412144818586, -50.0), (1653.4698060641144, 1944.1418295926082, -50.0), (1681.9218895646338, 1971.0958317170816, -50.0), (1747.0431008981082, 2042.9273191112097, -50.0), (1822.0699290695136, 2091.905101628295, -50.0), (1835.9916271420313, 2101.0114705428364, -50.0), (1869.1541001462965, 2127.31800577785, -50.0)], [(1579.4667968301937, 1885.2412144818586, -50.0), (1637.9972218324817, 1943.5937844120556, -50.0), (1703.282950654957, 1991.63180574286, -50.0), (1738.8093107904954, 2037.447210530409, -50.0), (1794.5164827322942, 2102.7170826808992, -50.0), (1862.1595318722864, 2168.0946488192617, -50.0)], [(1637.9972218324817, 1943.5937844120556, -50.0), (1700.141722573284, 2000.0442235761263, -50.0), (1772.9408053824018, 2067.4342877447034, -50.0), (1824.3408958415364, 2102.844760991809, -50.0), (1897.3022297535838, 2166.793446724411, -50.0), (1938.1612628726714, 2201.2668641986925, -50.0)], [(1700.141722573284, 2000.0442235761263, -50.0), (1721.143470850444, 2016.2264006509645, -50.0), (1793.526714422542, 2083.6120514345866, -50.0), (1860.101928927344, 2152.349122277539, -50.0), (1932.428101089616, 2217.5536539248124, -50.0), (1990.1070509526762, 2268.091401416414, -50.0)], [(1721.143470850444, 2016.2264006509645, -50.0), (1741.3365873854007, 2044.2352478867535, -50.0), (1795.075669188179, 2102.5321215693943, -50.0), (1858.0873642836677, 2166.844447659484, -50.0), (1917.373764479797, 2216.1370353156067, -50.0), (1947.9607303034359, 2242.536988353667, -50.0), (1999.2895226333872, 2299.03620332544, -50.0)], [(1741.3365873854007, 2044.2352478867535, -50.0), (1800.9249314134781, 2111.9438115536127, -50.0), (1835.5622316209171, 2157.700227678026, -50.0), (1885.0868965019847, 2221.233855938515, -50.0), (1917.0327159911644, 2248.072115258994, -50.0), (1957.4560845501164, 2290.901851210921, -50.0), (2005.7271454102442, 2340.6610344947667, -50.0)], [(1800.9249314134781, 2111.9438115536127, -50.0), (1865.4824386740686, 2171.856558003098, -50.0), (1918.4307952688266, 2238.7647207536056, -50.0), (1983.5137328386445, 2287.028620104539, -50.0), (2043.001185238109, 2340.3627133496266, -50.0), (2075.2639750188982, 2386.0408462639693, -50.0)], [(1865.4824386740686, 2171.856558003098, -50.0), (1915.2637195330217, 2225.7271824045606, -50.0), (1944.8940048320405, 2267.1375458914395, -50.0), (1985.433183807592, 2311.6425643369894, -50.0), (2032.9487748774009, 2361.153316386769, -50.0), (2078.2140160507047, 2426.6514214749727, -50.0), (2111.196876036598, 2478.836990805713, -50.0)], [(1915.2637195330217, 2225.7271824045606, -50.0), (1980.8266983269755, 2291.3274427283372, -50.0), (2040.3638760785002, 2357.351381034711, -50.0), (2109.3756204210745, 2407.4496986140775, -50.0), (2168.921543070233, 2446.8473827835946, -50.0), (2199.8752843224165, 2495.793444503929, -50.0)], [(1980.8266983269755, 2291.3274427283372, -50.0), (2031.3283331548487, 2367.2334727344637, -50.0), (2099.0791013707076, 2420.07717279649, -50.0), (2178.319882830665, 2476.656251989065, -50.0), (2229.6579676322945, 2519.101854973498, -50.0), (2259.884404713406, 2546.543151906546, -50.0), (2300.0, 2600.0, -50.0)]]

draw2(graph, init, goal, trail)