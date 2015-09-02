import _winreg
import sys
import os

IDAQICO = "0000010001003030000000000000a82500001600000028000000300000006000000001002000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007d7e980c646a8c7b314274f4294479ff4a6593ff6a87a9ff7e9fb5ff96acbeffa2b5c5ffa7b9caffabbdceffb0c1d2ffaec2d1ffb1c5d4ffafc3d2ffb0c3d3ffafc5d3ffadc3d2ffb1c3d4ffa9bed0ffa5b9cbff9fb3c5ff96adc1ff8ea0baff8096b3ff758db1ff6f89afff7993b4ff8597b7ff8294b5ff778eb2ff6a82a9ff607ca1ff6b839fff4f6077ff607186ff607995f874859e9179889c0c0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000656d8f2f374978c72d3f74fe405d8bff6382a1ff8198b3ff92a9beff9baec2ffa2b6c7ffa8bbcaffacbfcdffabc1cfffadc1cfffaec1d0ffadc2d1ffaec2d1ffabbfd0ffa8bdcfffa5b8caff97b2c4ff97abbeff8d9cb8ff7c90b1ff6e89adff768eb4ff7d95b4ff8798b4ff7f94b4ff738db2ff607ba3ff446393ff4c6b8bf57f8a9d9676889be38793a551848ba001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006f789c115259858a274074f53c5587ff5f7a9eff7d95b1ff8da1bbff97aabeff9fb4c3ffa8b7c9ffabbbceffabbfceffb2bfd0ffaabfd0ffaec2d2ffadbfd1ffa8bacdffa6b6cbff93b1c5ff97a7beff8796b5ff7a8db1ff718aaeff7791b2ff8599b7ff7f98b7ff7b94b1ff6b86b1ff496088ff334e7eff49607ec86f7f900284909f11000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000008687a403616d9133314572a2264578f6486290ff6781a9ff7b95b6ff88a5bdff96adc3ffa0b6caffa9bbcdffa8bdcfffa9bfd1ffaac0d1ffabbed0ffa6b9ccffa1b3c8ff95adc3ff8ea1baff8093b2ff7b8eb0ff7790b0ff7c95b5ff8397b7ff7b96b4ff6c8db2ff475e8aff1f2e59ff475e8cff4b627db000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005e668b02626b92691a2f60fd2b5082ff4e78a3ff678daeff849ebaff93adc2ffa0b7ccffa2bbcdffacbed1ffabbfd2ffa7bcceffa4b8caff9ab0c5ff95a6beff869cb6ff7a92afff7c92b2ff8093b0ff7f96b4ff7f98b8ff7290b3ff6280a8ff263156ff35446bff3c5380ff435a7392000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000706f8c3524244ffd273f71ff4e709cff708caeff839bb6ff94aabfffa0b6caffa5bbcdffabbcceffadbfd1ffaabccfffa4b7caff9bb0c5ff91a1baff7c97b2ff7994b0ff7c94b2ff8695b1ff8495b4ff5d769bff476892ff37496eff1b1d37ff232d4dff223156f95a6b81390000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004341665f1f224aff28406cff51749bff7894b0ff92a9beffa1b6c7ffa8bdcfffb1c2d3ffadc0d1ffb2c1d2ffabbccfffa4b6c9ff9eb0c6ff8b9fb9ff7c99b5ff7d95b3ff8195b3ff7e93b0ff7288adff42608eff5071a0ff2e3a60ff17182cff101322ff3d4454b40000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004340590333395baa2a3760ff283d6dff476591ff7290b1ff96aec4ffabbfcfffafc7d7ffb7c8d9ffb5c7d8ffb8c5d6ffaabed0ffa6b8cbff9bafc4ff899fbaff7e96b4ff7f94b3ff7e93b3ff7891b1ff5c74a0ff486998ff425a85ff232c4bff0d0c1bff11171fff2d343eb1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000076697b064040589a41506dfe4b6480ff5e7695ff5d7797ff6988a7ff829cb8ffabbed2ffb7cdddffb7ccddffbacadcffb7c7d8ffa7bdcfffa1b8cbff99aec3ff8aa1bbff8494b4ff8195b5ff7790b1ff657ca3ff36497bff3a4d75ff151c36ff15121fff100c17ff080f20ff414859bd000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000039384f09404864c7212f56ff233961ff446588ff6783a0ff8299b4ff7e93afff7e9bb6ff99b2c8ffb1c7d9ffbacbdcffb2c6d4ffacbecfff9cb9cbff98abc2ff819dbaff8697b6ff7f96b6ff6c86afff394d7eff3a4d77ff151d36ff0d101eff0b0b13ff10111bff151f30f9414c5d50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000393d64661b2754ff223563ff385886ff597ca0ff7f9ab4ff8faabeff8fa5beff879db5ff889cb9ff97b0c6ffa0b9cdffa5bdd0ff9ab2c9ff8ca4c1ff7798b7ff7a94b5ff688bb3ff4d6f9fff273462ff161527ff070712ff262e41f839455a80242c3f8c474c593a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002f2e556d1b2247ff25315aff34527fff587c9fff8aa5bbffa0becdffb0c2d5ffaabecfff9fafc4ff9ea8bfff7f92b2ff8ea8c2ff7e9fbcff7b9ebeff7895b6ff6287aeff4c709eff344a7bff0e142cff0a0807ff020408ff0c0b13ff242f43e64e5a713500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002b345a8d151c42ff1c224bff273e6aff4c6e90ff84a1b6ffa6bdcfffb5cad9ffbcd0e0ffbac7dbffa9b7cbff94a4baff96a4bbff7a94aeff7387abff5f7aa4ff3e618eff264271ff141534ff08070dff0c0b0fff07060bff070408ff0e131eff2d3b4d880000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000534769023d3f652e393f6d7128356de72c3c72ff37457aff2c4079ff364f82ff6580a3ff98b3c7ffb4ccdaffbbcfddffbbcddcffb8cadaffadbeceff9eadc2ff94a4baff909fb6ff798cabff384c7bff11193aff0a0913ff09080dff0d0b10ff09080dff060708ff070b15ff3a47577e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000716a89043f40698a334775f93b598aff425e92ff4a6a9aff6481aaff657ea7ff58739fff4f729bff7493b1ffa3bdd0ffb8ccdbffbad1dfffbbceddffb2c3d3ffa2b7caff93a3bcff788fa9ff7c96aeff5c6c91ff121121ff0c0f14ff0c0b10ff0b0a0eff0a090eff0a0e10ff0f1324fc434f622e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003b497154485b8cfc6988aeff7c99bdff8698bdff768fb3ff7d93b3ff8b9cbaff8798b7ff7690b3ff728ab0ff7e99b7ffa8c0d3ffbacfdeffb9ccddffb2c5d6ff99b3c6ff8b9eb9ff6985a5ff536f91ff576986ff15141fff0f0e17ff0e0910ff120f17ff0c0b12ff0e1523ff31384ec9535a71020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004b4a7506304471a9627da8ff8cabc6ff9bb4ceff9daecbff88a0bdff89a2bcff8da5beff91a6c0ff8da5bfff8b9ebcff7c97b5ff87a4baffb2c7d6ffb8cbd9ffa9bcd1ff5f7d9eff768bb1ff59759eff293b60ff222a3cff0e0a11ff131016ff0f1014ff101422ff232d43e9374661c15c687f2b636c840a6971870400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002f3a6688374f7ffc486492ff7392b0ff899eb9ff8ea3bdff89a1bbff90abc2ff94adc3ff92aec4ff90abc1ff92abc2ff8ea3bdff879fb7ff98b1c5ffb3c9d7ffa1b2caff8fa0baff8291b0ff4b5e85ff090d1dff09080dff0a090bff080a0fff04090aff090f1aff425067a05d6a8331364059cb262d44ea293144db3d45559d565a673700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000858fa5014b527a57364976f9455986ff33477dff47668fff6a83a5ff85a1bdff8caac3ff92aac4ff9aacc7ff95b0caff95afc9ff91aec7ff9aabc4ff96a5bfff8ba6beffa7bfd6ffa5b5caff97a3b1ff76859fff313e6aff0b0a0fff060709ff090c10ff0a0f12ff070a0eff090b0cff101823fe2e3443f310101fff0c0b14ff0f0c11ff111117ff1a1e29f5505a67650000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007c839f21303d6bea50678cff484f86ff2f408fff3c559eff5f7ab1ff81a2c4ff90adc9ff8ba6c0ff97abc4ff94b1c9ff96b1caff92afc9ff97aec7ff97aac3ff92a8c0ff99b4cbffa6b7cdff8b96a3ff5a6d93ff1d2951ff0b080eff06060aff07090eff05090eff08090dff05080cff05080cff0a0c10ff090a0eff05050cff0c0a0fff090d13ff111215ff1f2e3bf85b6f7d38000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064698d862d3e74fe5f7599ff343c74ff273587ff2b4599ff3c57a4ff405e97ff6280a6ff86a4beff97afc9ff93afc8ff97b0ccff90aecbff96acc6ff95adc5ff96a9c2ff95acc2ff9eb2ccff6d83a1ff455988ff1b2144ff0a0709ff08070cff05070bff03060aff08090eff05060aff06060aff18191aff171819ff181a1bff08090aff050a0fff0d090cff121929ff5b6f7f7d00000000000000000000000000000000000000000000000000000000000000000000000000000000878da702434172d2334c88ff4f6994ff3b5188ff4d6ca7ff637bb1ff85a4c7ff91abcbff8ba8c4ff8ba9c8ff8fabcaff90aacaff92a8cbff94aacfff90a9c9ff8fabc7ff91a7c0ff94a8bdff8e9fbdff365280ff253871ff1d2245ff0b0b0fff07070bff04060bff070a0fff080a0eff050408ff070307ff070608ff070809ff080a0bff0a090aff030409ff0b0507ff0d1221ff637486af66717f2c7e89950200000000000000000000000000000000000000000000000000000000000000006673951426316bf4445d91ff596d99ff21355cff5c789fff88a7c7ff9eb7d1ffa6b9d0ff95b2cbff8eabc7ff8aaccaff8ca9caff8aa9cdff93aad1ff91a9ceff91accbff92adc7ff94a3bfff6a81aaff4d77a4ff39588fff212b58ff0b0d13ff0b0a0eff0a090bff090d0fff050408ff08070bff060509ff050406ff030204ff050406ff040305ff07060bff09080bff121317ff181c2bff1c2230fb4a4f59a5868b9409000000000000000000000000000000000000000000000000000000004953793b2e3d76fd5672a0ff546593ff242e5eff30467fff5b7ca8ff8aa4c4ff9fb7d1ff92b2cbff96b1cfff95aecfff8dadd0ff8babd0ff8eacd2ff8babcfff92acccff92aec7ff899ebaff6b88adff6b89adff6582aaff3b5189ff24315fff121833ff070908ff08070aff050408ff07060aff07060aff060508ff060507ff070608ff050407ff060509ff060509ff07060aff07070dff090a0fff0d0e13ff434b53d7606a781b000000000000000000000000000000007098b0145e779240435179953f5489ff6883acff4e6397ff6a83b0ff7586b6ff55629bff5b76aaff89a3c7ff9eb5cfff99b6d1ff9cb2d1ff95b2d3ff94afd1ff93b0d3ff92b1d2ff93b1cdff93afccff7a8fb1ff3a517fff304272ff344678ff1b2e6aff2a3662ff1a2043ff080912ff08070aff0b0a0eff08070cff07050aff09080bff070608ff050406ff060508ff08070bff08070bff0c0b10ff0a0c0fff0c0d10ff0a090cff0d1316ff33425198000000000000000000000000000000005d7f99486b819bc6384a73f94b6395ff6e8aafff6775a1ff8aacc8ffa8c0d2ff9cb5d2ff98b2cfff9fb9d3ffabbdd6ffa3bcd5ffa6bcd7ff9ebbd7ff9fb9d5ffa2b8d5ff9fb8d4ff97b9d1ff94adcdff5977a0ff4a5f8dff39436aff2a3466ff2b3569ff1b1d3dff171a34ff0b0c17ff0b1011ff0c0f14ff0c0c13ff0b070dff08060aff0e0c0fff070608ff070709ff06060aff09090dff141418ff0a0c10ff0c0c13ff090810ff0a0b0dff243441d2566a7703000000000000000000000000566f898f677d96cd3c4d76f2596e9eff7491b4ff767faaff587fa7ffa3c1d3ffa1b9d0ffa3bad3ffa4bed4ffadc2d5ffafc6daffa8c1daffa3bfd8ffa3bfd7ffa7bfd7ffa6bfd7ffa1bdd5ffa0b4d0ff59709dff445d8cff272d55ff1c2344ff15223eff121121ff0a0b15ff070a0cff070a0bff070c12ff0b0d14ff0b080fff0a080dff09080bff060607ff060708ff06070bff090a0eff18191dff0a0a0dff0f0c17ff0e0d15ff0a0c0fff1e2e39db506673050000000000000000716c840162728b94667890c037456eeb6178a6ff7b94b5ff838eb4ff3d5c8cff96b9d1ffa6bed3ffa3bad2ffa7c2d5ffb1cbdaffb1cadbffa1bed5ffa2bbd4ffa1bbd3ffa5c0d8ffaac5dbffacc5d8ffa0bcd2ff5c729eff455f8dff384164ff10121fff0a131aff0e0b0fff0e0e0fff0b0a0eff0a0b0fff0a0d13ff0b0c12ff0d0b12ff0a090eff060509ff050506ff040406ff06070cff0b0c10ff101115ff080a0cff0d0e18ff0e0f18ff090b0dff2a313cb569828e010000000000000000000000005f677fa5333e58ea222d56ff647ba7ff7c91b1ff8190b1ff55628fff6f8aacffaac8dcffa7b8d2ffa3bed2ffabcbd9ffa4bed2ff91a9c4ff86a3c1ff8dacc6ff9bb6cfffa2c1d5ffaac6d6ffa1bcd1ff6982abff293c68ff283455ff161628ff0a0d19ff0a0a0fff06060bff080912ff070b0fff0a0a10ff0b0b11ff0c0c13ff08070dff060509ff050406ff050507ff040509ff0b0d11ff191a1eff070b0cff0d0f18ff0d1119ff0a0b0eff19202ff0506e791900000000000000000000000055536c84090e20ff182345ff506899ff526b97ff667da0ff6b769bff3b5482ff98bcd0ffaebbd4ffa3b4cbffaac1d5ff849ebcff7d98b5ff7388a2ff647893ff84a0bdff8caec7ff98b8ccff96adc7ff576f9aff475d86ff2d395aff15162cff0d0d17ff090b13ff0b090fff08070bff0a080dff0a080dff09080dff0b0a0fff09070cff07060bff06050aff06060bff030409ff0c0d11ff0a0b0fff08080aff0b0a14ff070a11ff0c0f17ff142434fa596b792900000000000000006c6478672e2d40f9070b14ff161f39ff2e4372ff4c5b83ff475473ff667296ff334371ff6b8eaaffa8bed5ff91a7c2ff899dbdff6175a4ff7d8cacff434964ff252849ff596c8eff829ebcff8598b8ff8898baff637ca3ff2d3c64ff181833ff171323ff100e14ff090a0fff0b090eff09080cff0d0b10ff0a090dff0c0b10ff0e0d12ff0d0c11ff0a090eff09080dff08080cff06070aff0c0d11ff06070bff070609ff07070dff0b0e16ff0b1421ff2b3a4aa34858670200000000646273043b3b4cd00f111bff0f0d16ff1b1d37ff29355eff303553ff23273dff4a5379ff353860ff56718bff9bb8ceff96afcaff7f92b3ff798bb5ff8190b7ff7c93b1ff90a8c1ff889fbbff8397b3ff949ebeff8497b5ff415177ff273355ff20233bff141627ff0f0d14ff0e0c0eff0c0b10ff0c0b0fff0c0b10ff121116ff110f14ff111014ff111015ff0d0c11ff0b0a0fff0c0c10ff0a0b0fff202226ff121317ff0c0b0fff090b0dff0c0e17ff202d3eb1414f5f0600000000000000005c63740c161929ea0c0c0eff0a0a12ff282f4eff3e5380ff56688cff5f7699ff506589ff2d355cff607595ff94b2c7ff95abc3ff7d8caeff788bb0ff7c93b6ff7f99b7ff819db8ff8a9cb8ff899bb8ff7e91b0ff546c91ff263b65ff232f4eff292c48ff131527ff131117ff0f0c0fff0a0a0eff090a0eff0b0e12ff121015ff19181dff131116ff0f0e12ff0f0d12ff0e0d12ff09090dff0f1114ff202125ff1d1e23ff252629ff202325ff171b22ff32455176000000000000000000000000737a8c011a1c2db60b0b0dff09090fff222f51ff536996ff647396ff576d8dff3a3d5fff2e4467ff7b8eaeff8eaec0ff99adc4ff7d8dadff566c92ff526c93ff4f638eff4b638eff506891ff4e6b95ff52739dff496a93ff3a517eff253056ff11132eff121522ff0b0c10ff08070bff04050aff07080dff080a0fff0d0c10ff100e13ff0c0b10ff0f0e12ff0c0a0fff0b0a0fff0a0a0dff18191cff111215ff0a0b10ff0a090eff0f0f12ff0c0f18ff3243508700000000000000000000000079819507333446c90d0c11ff08080eff181d37ff1c2b56ff252a4cff1a254aff343f64ff647c9bff8ba0bbff98b0c6ff9eb1c7ff98aec6ff7e97b3ff6785a5ff5e779cff617da0ff728aa8ff7f9bb9ff82a0bfff6785abff3d5481ff343f65ff191b2bff0b0f14ff060b0eff04070bff090c11ff0a0b0fff0b0b0fff0d0b10ff0c0a0fff09070dff08070cff07060aff0a090dff0d0d11ff1a1c20ff05070bff05060bff110d12ff100f11ff0b0b14ff223041e26c818c0900000000000000004a556b620c0d1dfe0e0b11ff090a10ff1c2239ff42537dff515f87ff5f6d92ff6e83a6ff8799b6ff92a9beffa3b3cbffa2b7ccff9eb8ccff9cb5cbff97b5cbff95b1c8ff94b2caff9db5cbff9bb0c9ff7f99b7ff667ca3ff303f64ff242e49ff0c0d17ff0a0b0eff070a0dff06080dff08090eff090b0fff0a0c11ff0d0e13ff090a0eff0b090eff07080dff0b0a0eff0d0c10ff141419ff131217ff0c0d12ff080a0fff0a090eff0f0b13ff141423ff303e50c56c8590040000000068697c02373a4fa6060811ff0e0910ff090b11ff121727ff394b76ff697aa1ff7886a8ff8398b5ff8da2bcff9cb0c5ffa6b7ceffa5bdd2ffa6bed3ffa8bdd2ffa2bdd2ffa0bbd0ff9fbacfffa5becfff8da2c0ff567398ff334465ff0f152aff0b0e16ff0a0a0fff0b0a0eff07060aff09080cff08070cff0b0d12ff12161bff0b0f15ff08090eff0b0a0eff0d0c10ff0c0a0fff121115ff121113ff09080bff0a0d10ff0d1115ff131525ff18182bff232b3fef616d7d3800000000000000006a667902342f45ac0b0c15ff0f0a11ff0f1118ff121721ff2c3e64ff697b9fff818eaeff899fb9ff92aac1ffa2b5caffa8bed1ffa7c3d6ffb1cadcffb1c7d9ffaac3d6ffadc5d7ffabc1d3ffa3baceff64769fff2b4066ff131a2bff13141aff141211ff100e12ff0d0c11ff0c0a0fff0c0b0fff0d0c11ff0a0d12ff0d1116ff0c1015ff080a0fff0c0b10ff0c0b0eff191e27ff090c15ff0d0c10ff0a0c10ff0b0e16ff0f151fff192539f02d364db04f5d6e3e00000000000000000000000000000000322c4686090c14ff171419ff0c0f15ff0d1016ff2e3f60ff667b9eff7e92afff91a5bdff9eafc4ffa0bbcfffabc4d6ffabc9daffb5cedfffafcadcffb3ccddffb4c7d9ffa5b9cfff738faeff42507eff1d213dff0d0f1bff0d0f14ff121014ff0b090eff0c0b10ff0e0d11ff0d0c11ff0f0e13ff111318ff0e1217ff090d12ff08090dff0c0a0fff0b0d16ff2b3847c91e2b3cde0e111dff101220ff1b1e30ff1d2538f9536b794677809302000000000000000000000000000000000000000052495b281d1a27f0101319ff11151bff040812ff161d34ff4a638aff7391afff8ea3bcffa1b4c8ffa2bfd2ffacc7d8ffb0ccdcffb8d1dfffb2d0ddffb1c9d9ff9dadc8ff6f86a8ff415980ff1f294cff0c0e18ff0b0f14ff121318ff131116ff0e0c11ff0d0c11ff0b0a0fff0b0a0fff0d0c11ff17151aff121116ff0b0c11ff140d13ff0f0d11ff131b28ff5162707d516178233a455b85334055ca2a374fa13c52643200000000000000000000000000000000000000000000000000000000000000003e314847141224fa141920ff151821ff0f0f19ff1d2c48ff5e81a4ff85a1bbff9ab2c7ffa8bfd3ffadcadaffb6d1e1ffbad3e1ffb5cdddff8da0bdff4f597dff2c3751ff151c35ff090d20ff0a0f13ff11151aff1a1c20ff131217ff0d0c11ff0d0c10ff0c0a0fff0a080dff0d0b10ff121115ff141318ff0f1014ff130f15ff0d1018ff23313dec63727e0d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000675c70041e1a2fdc100c18ff18171dff0f141eff0d111fff334f72ff7a95b3ff90aec3ffa2bbcfffafc7d8ffb5cedeffb7d4e1ff9eacc6ff354665ff13192cff111318ff101015ff0d0f13ff090b12ff0c0f14ff16181dff131217ff111014ff0d0c11ff0c0b10ff0b0a0fff0e0d12ff111015ff18161bff18181aff14131bff131a26fe4055608200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000041364f950f0a14ff0d1012ff161a21ff12131fff151b33ff476384ff748cb0ff779bb5ff9db5ccffadc5d4ffa6bdcfff5f6884ff121425ff0e0e1aff0c0d10ff080a0dff0b0c11ff0c0d12ff0c0e12ff0d0e13ff0e0f14ff0b0c0fff0d0c0fff0e0a0fff0d090fff0e0e13ff101216ff131418ff161619ff181f27f7445661915a727d05000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000584d6522241f34dd090d17ff10111aff221b24ff23181eff111a26ff2a3754ff516c8aff526d91ff6a8aabff8295b3ff363d5bff0e0f1bff0a0b16ff0a0c0fff0a0c10ff0c0e13ff121418ff17181dff1b1c20ff14161aff0f0e14ff0b0a11ff0b0b10ff0f0c11ff151018ff12121efe171a29e82433409c535d692f6d7b85020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000453d5412332e41991c1a2bfc131222ff131722ff11131cff13111cff161424ff11192bff162d47ff44587bff222a48ff111219ff0e0f18ff080b0eff090a0fff0b0d12ff0d0f14ff121419ff181a1eff15171bff121015ff111219ff0d131dff1f2c36ef2a3a447a3847552e2637480d000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006b6a7b2a585a6c782d3347f5131121ff16131dff18161eff0e1418ff0d1115ff141926ff25273aff171720ff0f1019ff0c0f13ff0d1115ff111217ff0a0e13ff0e1214ff111518ff11161cff161923ff1c2531f6373e4b93505763130000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007473874139394db31c1c2eea0b1422ff131622ff121620ff0f141cff161a2afe2d3343f612182aff121723ff12121aff13111bff111420fe151a2dfe22273ae935374ccd474d5d88525b6a2d000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005b526417494559574c455c6b3d374b86464251935452603f64647419403b524e3a374e962e31479f373e559c3b465c604b5267435f63781366667d020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000fe0000000003a4ecff8000000007a4ecffc00000001fa4ecffe00000007fa4ecfff80000007fa4ecfffc0000007fa4ecfffc000000ffa4ecfff8000000ffa4ecfff0000000ffa4ecfff0000000ffa4ecfff8000001ffa4ecfff8000003ffa4ecfff8000003ffa4ecffc0000003ffa4ecff80000003ffa4ecff80000003ffa4ecff00000001ffa4ecff000000007fa4ecfc000000003fa4ecfc000000001fa4ecfc000000001fa4ecf80000000007a4ecf80000000003a4ecf80000000001a4ece00000000001a4ece00000000000a4ece00000000000a4ecc00000000000a4ece00000000000a4ece00000000000a4ecc00000000000a4ec800000000001a4ec800000000003a4ec800000000003a4ec800000000001a4ec800000000001a4ec000000000003a4ec000000000007a4ec80000000000fa4ec80000000003fa4ecc000000007ffa4ecc00000000fffa4ece00000000fffa4ece00000001fffa4ecf0000000ffffa4ecfc000007ffffa4ecff00001fffffa4ecffc0007fffffa4ec"
IDAQ64ICO = "0000010001003030000000000000a82500001600000028000000300000006000000001002000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007d7e980c646a8c7b314274f4294479ff4a6593ff6a87a9ff7e9fb5ff96acbeffa2b5c5ffa7b9caffabbdceffb0c1d2ffaec2d1ffb1c5d4ffafc3d2ffb0c3d3ffafc5d3ffadc3d2ffb1c3d4ffa9bed0ffa5b9cbff9fb3c5ff96adc1ff8ea0baff8096b3ff758db1ff6f89afff7993b4ff8597b7ff8294b5ff778eb2ff6a82a9ff607ca1ff6b839fff4f6077ff607186ff607995f874859e9179889c0c0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000656d8f2f374978c72d3f74fe405d8bff6382a1ff8198b3ff92a9beff9baec2ffa2b6c7ffa8bbcaffacbfcdffabc1cfffadc1cfffaec1d0ffadc2d1ffaec2d1ffabbfd0ffa8bdcfffa5b8caff97b2c4ff97abbeff8d9cb8ff7c90b1ff6e89adff768eb4ff7d95b4ff8798b4ff7f94b4ff738db2ff607ba3ff446393ff4c6b8bf57f8a9d9676889be38793a551848ba001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006f789c115259858a274074f53c5587ff5f7a9eff7d95b1ff8da1bbff97aabeff9fb4c3ffa8b7c9ffabbbceff8299caff586cc6ff4b63c5ff556cc7ff8094cbffa8bacdffa6b6cbff93b1c5ff97a7beff8796b5ff7a8db1ff718aaeff7791b2ff8599b7ff7f98b7ff7b94b1ff6b86b1ff486098ff2a449dff334b94d46f7f900284909f11000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000008687a403616d9133314572a2264578f6486290ff6781a9ff7b95b6ff88a5bdff849bc2ff223bbfff001abbff001abbff001abbff001abbff001abbff2841bfff899dc6ff95adc3ff8ea1baff8093b2ff7b8eb0ff7790b0ff7c95b5ff8397b7ff7b96b4ff6c8db2ff475e8aff0d1d74ff001abbff0f29b8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005e668b02626b92691a2f60fd2b5082ff4e78a3ff597eafff0923bcff001abbff0b25bdff425dc3ff576cc6ff3a51c3ff0621bcff001abbff132dbcff8c9dbeff869cb6ff7a92afff7c92b2ff8093b0ff7f96b4ff7f98b8ff7290b3ff6280a8ff263156ff213385ff001abbff001abbdf000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000706f8c3524244ffd273f71ff4e709cff1c38b6ff001abbff223bbeff96abc9ffa5bbcdffabbcceffadbfd1ff8499cbff0924bcff001abbff4959baff7c97b2ff7994b0ff7c94b2ff8695b1ff8495b4ff5d769bff476892ff37496eff1b1d37ff132372ff001abbff001abbdf0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004341665f1f224aff28406cff44669dff001abbff0a25bcff96acc7ffa8bdcfffb1c2d3ffadc0d1ffb2c1d2ffabbccfff6578c4ff001abbff0923bbff7995b5ff7b93b3ff798eb4ff768cb1ff6d83afff3d5b90ff4c6da2ff2b3866ff161835ff0a1660ff001abbff001abbe1001abb10001abb10001abb0200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004340590333395baa2a3760ff283d6dff223e9eff001abbff3b54c0ffabbfcfffafc7d7ffb7c8d9ffb5c7d8ffb8c5d6ffaabed0ff9dafcaff001abbff001abbff687eb5ff5d75b5ff001abbff001abbff001abbff001abbff001abbff001abbff001abbff001abbff001abbff001abbff001abbff001abbff001abb200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000076697b064040589a41506dfe4b6480ff5e7695ff2a44adff001abbff4862bfffabbed2ffb7cdddffb7ccddffbacadcffb7c7d8ffa7bdcfffa1b8cbff001abbff001abbff6475b5ff6177b7ff001abbff001abbff001abbff001abbff001abbff001abbff001abbff001abbff001abbff001abbff001abbff001abbff001abb200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000039384f09404864c7212f56ff233961ff446588ff1b35b6ff001abbff3049b7ff7e9bb6ff99b2c8ffb1c7d9ffbacbdcffb2c6d4ffacbecfff88a8c9ff001abbff001abbff6b7eb7ff7189b6ff0a26bbff001abbff0822b1ff0e184bff0a123dff070d34ff0b1239ff07166eff001abbff001abbe5001abb30001abb30001abb060000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000393d64661b2754ff223563ff385886ff1430b3ff001abbff0b26beff7d94bfff879db5ff889cb9ff97b0c6ffa0b9cdffa5bdd0ff4c68c3ff001abbff0823bbff7690b5ff688bb3ff3859a8ff001bbbff001abbff04126dff262e41f839455a80242c3f8c22318594001abbff001abbdf00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002f2e556d1b2247ff25315aff34527fff1230b3ff001abbff001abbff162fbdff8397c7ff9fafc4ff9ea8bfff7d90b1ff516dc2ff041fbcff001abbff3750b9ff6287aeff4c709eff344a7bff081975ff001abbff001abaff09124aff242f43e64e5a7135001abb60001abbff001abbdf00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002b345a8d151c42ff1c224bff273e6aff0d2aacff001abbff445cc4ff1029beff001abbff152fbdff2239bfff041fbbff001abbff001abbff152eb6ff5c77a4ff3e618eff264271ff141534ff08070dff04178aff001abbff0019afff0d1535ff2d3b4d88001abb60001abbff001abbdf0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000534769023d3f652e393f6d7128356de72c3c72ff37457aff2c4079ff132da1ff001abbff4962c4ffa1b9d6ff3e57c6ff021dbcff001abbff001abbff0620bcff4359bcff8d9cb7ff798cabff384c7bff11193aff0a0913ff09080dff0c0d20ff0118a6ff001abbff011899ff3948617e001abb60001abbff001abbdf00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000716a89043f40698a334775f93b598aff425e92ff4a6a9aff6481aaff657ea7ff344eafff001abbff2442bdffa3bdd0ffb8ccdbffacc2dcff8ca1d5ff889ccfff9bb0c9ff93a3bcff788fa9ff7c96aeff5c6c91ff121121ff0c0f14ff0c0b10ff0b0a0eff070d38ff001abaff001abbff0d25b49b001abb60001abbff001abbdf000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003b497154485b8cfc6988aeff7c99bdff8698bdff768fb3ff7d93b3ff8b9cbaff697ab9ff001abbff0320baff7893b7ffa8c0d3ffbacfdeffb9ccddffb2c5d6ff99b3c6ff7488bbff405db0ff43619dff576986ff15141fff0f0e17ff0e0910ff120f17ff0c0b12ff071663ff001abbff001abbff001abbb7001abbff001abbdf0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004b4a7506304471a9627da8ff8cabc6ff9bb4ceff9daecbff88a0bdff89a2bcff8da5beff91a6c0ff102bbcff001abbff415db6ff87a4baffb2c7d6ffb8cbd9ffa9bcd1ff5f7d9eff253eb7ff001abbff09209fff222a3cff0e0a11ff131016ff0f1014ff101422ff232d43e9374661c11c33adb9001abbff001abbff001abbff001abbdf0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002f3a6688374f7ffc486492ff7392b0ff899eb9ff8ea3bdff89a1bbff90abc2ff94adc3ff92aec4ff5370c0ff001abbff011cbbff5570b8ff98b1c5ffb3c9d7ffa1b2caff5a70b5ff021cbbff001abbff04105bff09080dff0a090bff080a0fff04090aff090f1aff425067a05d6a8331323d61d2021aa8ff001abbff001abbff021dbadf00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000858fa5014b527a57364976f9455986ff33477dff47668fff6a83a5ff85a1bdff8caac3ff92aac4ff9aacc7ff95b0caff93adc9ff2543beff001abbff001abbff1f3bbdff415ac7ff2840bfff001abbff001abbff0219a2ff0b0a13ff060709ff090c10ff0a0f12ff070a0eff090b0cff101823fe2e3443f310101fff090d31ff001ab5ff001abbff061fadf9505a67650000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007c839f21303d6bea50678cff484f86ff2f408fff3c559eff5f7ab1ff81a2c4ff90adc9ff8ba6c0ff97abc4ff94b1c9ff96b1caff8caac8ff3f58c0ff031ebcff001abbff001abbff001abbff001abbff162eb1ff192556ff0b080eff06060aff07090eff05090eff08090dff05080cff05080cff0a0c10ff090a0eff05050cff050f4fff001abbff0119a6ff1f2e3bf85b6f7d38000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064698d862d3e74fe5f7599ff343c74ff273587ff2b4599ff3c57a4ff405e97ff6280a6ff86a4beff97afc9ff93afc8ff97b0ccff90aecbff96acc6ff869fc4ff6378c0ff536bbeff5970c4ff556ca5ff445988ff1b2144ff0a0709ff08070cff05070bff03060aff08090eff05060aff06060aff18191aff171819ff181a1bff08090aff040e34ff0a0c32ff121929ff5b6f7f7d00000000000000000000000000000000000000000000000000000000000000000000000000000000878da702434172d2334c88ff4f6994ff3b5188ff4d6ca7ff637bb1ff85a4c7ff91abcbff8ba8c4ff8ba9c8ff8fabcaff90aacaff92a8cbff94aacfff90a9c9ff8fabc7ff91a7c0ff94a8bdff8e9fbdff365280ff253871ff1d2245ff0b0b0fff07070bff04060bff070a0fff080a0eff050408ff070307ff070608ff070809ff080a0bff0a090aff030409ff0b0507ff0d1221ff637486af66717f2c7e89950200000000000000000000000000000000000000000000000000000000000000006673951426316bf4445d91ff596d99ff21355cff5c789fff88a7c7ff9eb7d1ffa6b9d0ff95b2cbff8eabc7ff8aaccaff8ca9caff8aa9cdff93aad1ff91a9ceff91accbff92adc7ff94a3bfff6a81aaff4d77a4ff39588fff212b58ff0b0d13ff0b0a0eff0a090bff090d0fff050408ff08070bff060509ff050406ff030204ff050406ff040305ff07060bff09080bff121317ff181c2bff1c2230fb4a4f59a5868b9409000000000000000000000000000000000000000000000000000000004953793b2e3d76fd5672a0ff546593ff242e5eff30467fff5b7ca8ff8aa4c4ff9fb7d1ff92b2cbff96b1cfff95aecfff8dadd0ff8babd0ff8eacd2ff8babcfff92acccff92aec7ff899ebaff6b88adff6b89adff6582aaff3b5189ff24315fff121833ff070908ff08070aff050408ff07060aff07060aff060508ff060507ff070608ff050407ff060509ff060509ff07060aff07070dff090a0fff0d0e13ff434b53d7606a781b000000000000000000000000000000007098b0145e779240435179953f5489ff6883acff4e6397ff6a83b0ff7586b6ff55629bff5b76aaff89a3c7ff9eb5cfff99b6d1ff9cb2d1ff95b2d3ff94afd1ff93b0d3ff92b1d2ff93b1cdff93afccff7a8fb1ff3a517fff304272ff344678ff1b2e6aff2a3662ff1a2043ff080912ff08070aff0b0a0eff08070cff07050aff09080bff070608ff050406ff060508ff08070bff08070bff0c0b10ff0a0c0fff0c0d10ff0a090cff0d1316ff33425198000000000000000000000000000000005d7f99486b819bc6384a73f94b6395ff6e8aafff6775a1ff8aacc8ffa8c0d2ff9cb5d2ff98b2cfff9fb9d3ffabbdd6ffa3bcd5ffa6bcd7ff9ebbd7ff9fb9d5ffa2b8d5ff9fb8d4ff97b9d1ff94adcdff5977a0ff4a5f8dff39436aff2a3466ff2b3569ff1b1d3dff171a34ff0b0c17ff0b1011ff0c0f14ff0c0c13ff0b070dff08060aff0e0c0fff070608ff070709ff06060aff09090dff141418ff0a0c10ff0c0c13ff090810ff0a0b0dff243441d2566a7703000000000000000000000000566f898f677d96cd3c4d76f2596e9eff7491b4ff767faaff587fa7ffa3c1d3ffa1b9d0ffa3bad3ffa4bed4ffadc2d5ffafc6daffa8c1daffa3bfd8ffa3bfd7ffa7bfd7ffa6bfd7ffa1bdd5ffa0b4d0ff59709dff445d8cff272d55ff1c2344ff15223eff121121ff0a0b15ff070a0cff070a0bff070c12ff0b0d14ff0b080fff0a080dff09080bff060607ff060708ff06070bff090a0eff18191dff0a0a0dff0f0c17ff0e0d15ff0a0c0fff1e2e39db506673050000000000000000716c840162728b94667890c037456eeb6178a6ff7b94b5ff838eb4ff3d5c8cff96b9d1ffa6bed3ffa3bad2ffa7c2d5ffb1cbdaffb1cadbffa1bed5ffa2bbd4ffa1bbd3ffa5c0d8ffaac5dbffacc5d8ffa0bcd2ff5c729eff455f8dff384164ff10121fff0a131aff0e0b0fff0e0e0fff0b0a0eff0a0b0fff0a0d13ff0b0c12ff0d0b12ff0a090eff060509ff050506ff040406ff06070cff0b0c10ff101115ff080a0cff0d0e18ff0e0f18ff090b0dff2a313cb569828e010000000000000000000000005f677fa5333e58ea222d56ff647ba7ff7c91b1ff8190b1ff55628fff6f8aacffaac8dcffa7b8d2ffa3bed2ffabcbd9ffa4bed2ff91a9c4ff86a3c1ff8dacc6ff9bb6cfffa2c1d5ffaac6d6ffa1bcd1ff6982abff293c68ff283455ff161628ff0a0d19ff0a0a0fff06060bff080912ff070b0fff0a0a10ff0b0b11ff0c0c13ff08070dff060509ff050406ff050507ff040509ff0b0d11ff191a1eff070b0cff0d0f18ff0d1119ff0a0b0eff19202ff0506e791900000000000000000000000055536c84090e20ff182345ff506899ff526b97ff667da0ff6b769bff3b5482ff98bcd0ffaebbd4ffa3b4cbffaac1d5ff849ebcff7d98b5ff7388a2ff647893ff84a0bdff8caec7ff98b8ccff96adc7ff576f9aff475d86ff2d395aff15162cff0d0d17ff090b13ff0b090fff08070bff0a080dff0a080dff09080dff0b0a0fff09070cff07060bff06050aff06060bff030409ff0c0d11ff0a0b0fff08080aff0b0a14ff070a11ff0c0f17ff142434fa596b792900000000000000006c6478672e2d40f9070b14ff161f39ff2e4372ff4c5b83ff475473ff667296ff334371ff6b8eaaffa8bed5ff91a7c2ff899dbdff6175a4ff7d8cacff434964ff252849ff596c8eff829ebcff8598b8ff8898baff637ca3ff2d3c64ff181833ff171323ff100e14ff090a0fff0b090eff09080cff0d0b10ff0a090dff0c0b10ff0e0d12ff0d0c11ff0a090eff09080dff08080cff06070aff0c0d11ff06070bff070609ff07070dff0b0e16ff0b1421ff2b3a4aa34858670200000000646273043b3b4cd00f111bff0f0d16ff1b1d37ff29355eff303553ff23273dff4a5379ff353860ff56718bff9bb8ceff96afcaff7f92b3ff798bb5ff8190b7ff7c93b1ff90a8c1ff889fbbff8397b3ff949ebeff8497b5ff415177ff273355ff20233bff141627ff0f0d14ff0e0c0eff0c0b10ff0c0b0fff0c0b10ff121116ff110f14ff111014ff111015ff0d0c11ff0b0a0fff0c0c10ff0a0b0fff202226ff121317ff0c0b0fff090b0dff0c0e17ff202d3eb1414f5f0600000000000000005c63740c161929ea0c0c0eff0a0a12ff282f4eff3e5380ff56688cff5f7699ff506589ff2d355cff607595ff94b2c7ff95abc3ff7d8caeff788bb0ff7c93b6ff7f99b7ff819db8ff8a9cb8ff899bb8ff7e91b0ff546c91ff263b65ff232f4eff292c48ff131527ff131117ff0f0c0fff0a0a0eff090a0eff0b0e12ff121015ff19181dff131116ff0f0e12ff0f0d12ff0e0d12ff09090dff0f1114ff202125ff1d1e23ff252629ff202325ff171b22ff32455176000000000000000000000000737a8c011a1c2db60b0b0dff09090fff222f51ff536996ff647396ff576d8dff3a3d5fff2e4467ff7b8eaeff8eaec0ff99adc4ff7d8dadff566c92ff526c93ff4f638eff4b638eff506891ff4e6b95ff52739dff496a93ff3a517eff253056ff11132eff121522ff0b0c10ff08070bff04050aff07080dff080a0fff0d0c10ff100e13ff0c0b10ff0f0e12ff0c0a0fff0b0a0fff0a0a0dff18191cff111215ff0a0b10ff0a090eff0f0f12ff0c0f18ff3243508700000000000000000000000079819507333446c90d0c11ff08080eff181d37ff1c2b56ff252a4cff1a254aff343f64ff647c9bff8ba0bbff98b0c6ff9eb1c7ff98aec6ff7e97b3ff6785a5ff5e779cff617da0ff728aa8ff7f9bb9ff82a0bfff6785abff3d5481ff343f65ff191b2bff0b0f14ff060b0eff04070bff090c11ff0a0b0fff0b0b0fff0d0b10ff0c0a0fff09070dff08070cff07060aff0a090dff0d0d11ff1a1c20ff05070bff05060bff110d12ff100f11ff0b0b14ff223041e26c818c0900000000000000004a556b620c0d1dfe0e0b11ff090a10ff1c2239ff42537dff515f87ff5f6d92ff6e83a6ff8799b6ff92a9beffa3b3cbffa2b7ccff9eb8ccff9cb5cbff97b5cbff95b1c8ff94b2caff9db5cbff9bb0c9ff7f99b7ff667ca3ff303f64ff242e49ff0c0d17ff0a0b0eff070a0dff06080dff08090eff090b0fff0a0c11ff0d0e13ff090a0eff0b090eff07080dff0b0a0eff0d0c10ff141419ff131217ff0c0d12ff080a0fff0a090eff0f0b13ff141423ff303e50c56c8590040000000068697c02373a4fa6060811ff0e0910ff090b11ff121727ff394b76ff697aa1ff7886a8ff8398b5ff8da2bcff9cb0c5ffa6b7ceffa5bdd2ffa6bed3ffa8bdd2ffa2bdd2ffa0bbd0ff9fbacfffa5becfff8da2c0ff567398ff334465ff0f152aff0b0e16ff0a0a0fff0b0a0eff07060aff09080cff08070cff0b0d12ff12161bff0b0f15ff08090eff0b0a0eff0d0c10ff0c0a0fff121115ff121113ff09080bff0a0d10ff0d1115ff131525ff18182bff232b3fef616d7d3800000000000000006a667902342f45ac0b0c15ff0f0a11ff0f1118ff121721ff2c3e64ff697b9fff818eaeff899fb9ff92aac1ffa2b5caffa8bed1ffa7c3d6ffb1cadcffb1c7d9ffaac3d6ffadc5d7ffabc1d3ffa3baceff64769fff2b4066ff131a2bff13141aff141211ff100e12ff0d0c11ff0c0a0fff0c0b0fff0d0c11ff0a0d12ff0d1116ff0c1015ff080a0fff0c0b10ff0c0b0eff191e27ff090c15ff0d0c10ff0a0c10ff0b0e16ff0f151fff192539f02d364db04f5d6e3e00000000000000000000000000000000322c4686090c14ff171419ff0c0f15ff0d1016ff2e3f60ff667b9eff7e92afff91a5bdff9eafc4ffa0bbcfffabc4d6ffabc9daffb5cedfffafcadcffb3ccddffb4c7d9ffa5b9cfff738faeff42507eff1d213dff0d0f1bff0d0f14ff121014ff0b090eff0c0b10ff0e0d11ff0d0c11ff0f0e13ff111318ff0e1217ff090d12ff08090dff0c0a0fff0b0d16ff2b3847c91e2b3cde0e111dff101220ff1b1e30ff1d2538f9536b794677809302000000000000000000000000000000000000000052495b281d1a27f0101319ff11151bff040812ff161d34ff4a638aff7391afff8ea3bcffa1b4c8ffa2bfd2ffacc7d8ffb0ccdcffb8d1dfffb2d0ddffb1c9d9ff9dadc8ff6f86a8ff415980ff1f294cff0c0e18ff0b0f14ff121318ff131116ff0e0c11ff0d0c11ff0b0a0fff0b0a0fff0d0c11ff17151aff121116ff0b0c11ff140d13ff0f0d11ff131b28ff5162707d516178233a455b85334055ca2a374fa13c52643200000000000000000000000000000000000000000000000000000000000000003e314847141224fa141920ff151821ff0f0f19ff1d2c48ff5e81a4ff85a1bbff9ab2c7ffa8bfd3ffadcadaffb6d1e1ffbad3e1ffb5cdddff8da0bdff4f597dff2c3751ff151c35ff090d20ff0a0f13ff11151aff1a1c20ff131217ff0d0c11ff0d0c10ff0c0a0fff0a080dff0d0b10ff121115ff141318ff0f1014ff130f15ff0d1018ff23313dec63727e0d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000675c70041e1a2fdc100c18ff18171dff0f141eff0d111fff334f72ff7a95b3ff90aec3ffa2bbcfffafc7d8ffb5cedeffb7d4e1ff9eacc6ff354665ff13192cff111318ff101015ff0d0f13ff090b12ff0c0f14ff16181dff131217ff111014ff0d0c11ff0c0b10ff0b0a0fff0e0d12ff111015ff18161bff18181aff14131bff131a26fe4055608200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000041364f950f0a14ff0d1012ff161a21ff12131fff151b33ff476384ff748cb0ff779bb5ff9db5ccffadc5d4ffa6bdcfff5f6884ff121425ff0e0e1aff0c0d10ff080a0dff0b0c11ff0c0d12ff0c0e12ff0d0e13ff0e0f14ff0b0c0fff0d0c0fff0e0a0fff0d090fff0e0e13ff101216ff131418ff161619ff181f27f7445661915a727d05000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000584d6522241f34dd090d17ff10111aff221b24ff23181eff111a26ff2a3754ff516c8aff526d91ff6a8aabff8295b3ff363d5bff0e0f1bff0a0b16ff0a0c0fff0a0c10ff0c0e13ff121418ff17181dff1b1c20ff14161aff0f0e14ff0b0a11ff0b0b10ff0f0c11ff151018ff12121efe171a29e82433409c535d692f6d7b85020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000453d5412332e41991c1a2bfc131222ff131722ff11131cff13111cff161424ff11192bff162d47ff44587bff222a48ff111219ff0e0f18ff080b0eff090a0fff0b0d12ff0d0f14ff121419ff181a1eff15171bff121015ff111219ff0d131dff1f2c36ef2a3a447a3847552e2637480d000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006b6a7b2a585a6c782d3347f5131121ff16131dff18161eff0e1418ff0d1115ff141926ff25273aff171720ff0f1019ff0c0f13ff0d1115ff111217ff0a0e13ff0e1214ff111518ff11161cff161923ff1c2531f6373e4b93505763130000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007473874139394db31c1c2eea0b1422ff131622ff121620ff0f141cff161a2afe2d3343f612182aff121723ff12121aff13111bff111420fe151a2dfe22273ae935374ccd474d5d88525b6a2d000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005b526417494559574c455c6b3d374b86464251935452603f64647419403b524e3a374e962e31479f373e559c3b465c604b5267435f63781366667d020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000fe0000000003a40fff8000000007a40fffc00000001fa40fffe00000007fa40ffff80000007fa40ffffc0000007fa40ffffc0000000fa40ffff80000000fa40ffff00000000fa40ffff00000000fa40ffff80000007fa40ffff80000007fa40ffff80000007fa40fffc00000007fa40fff800000007fa40fff800000007fa40fff000000007fa40fff000000007fa40ffc000000003fa40ffc000000001fa40ffc000000001fa40ff80000000007a40ff80000000003a40ff80000000001a40fe00000000001a40fe00000000000a40fe00000000000a40fc00000000000a40fe00000000000a40fe00000000000a40fc00000000000a40f800000000001a40f800000000003a40f800000000003a40f800000000001a40f800000000001a40f000000000003a40f000000000007a40f80000000000fa40f80000000003fa40fc000000007ffa40fc00000000fffa40fe00000000fffa40fe00000001fffa40ff0000000ffffa40ffc000007ffffa40fff00001fffffa40fffc0007fffffa40f"

def DropIcos():
  with open(os.path.join(sys.argv[1], 'idaq.ico'), 'wb') as ico:
    ico.write(IDAQICO.decode('hex'))
  with open(os.path.join(sys.argv[1], 'idaq64.ico'), 'wb') as ico64:
    ico64.write(IDAQ64ICO.decode('hex'))

def InstallSelf():
  rootkey = _winreg.OpenKey(_winreg.HKEY_CLASSES_ROOT, "*")
  shellkey = _winreg.CreateKey(rootkey, "shell")

  peskey = _winreg.CreateKey(shellkey, "Open with IDA")
  cmdkey = _winreg.CreateKey(peskey, "command")
  _winreg.SetValue(cmdkey, "", _winreg.REG_SZ, os.path.join(sys.argv[1], 'idaq.exe') + ' "%L"')
  _winreg.SetValueEx(peskey, "Icon", 0, _winreg.REG_SZ, os.path.join(sys.argv[1], 'idaq.ico'))

  peskey64 = _winreg.CreateKey(shellkey, "Open with IDA64")
  cmdkey64 = _winreg.CreateKey(peskey64, "command")
  _winreg.SetValue(cmdkey64, "", _winreg.REG_SZ, os.path.join(sys.argv[1], 'idaq64.exe') + ' "%L"')
  _winreg.SetValueEx(peskey64, "Icon", 0, _winreg.REG_SZ, os.path.join(sys.argv[1], 'idaq64.ico'))

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print 'USAGE: idahere.py IDA_DIR'
  DropIcos()
  InstallSelf()
