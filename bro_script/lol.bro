module LoL;

@load base/protocols/dns



export {
    reduf enum Log::ID += { LOG };
    #type ports_to_dos: record {
    #    ports: string &log &optional;
    #    };

    type Info: record{ 
        ts: time &log;
        origin: string &log;
        origin_port: string &log;# 51463,58512,51674, so 51000-51999
        #ports: ports_to_dos &log &optional;
        query: string &log;
        };
    }
event bro_init(){
    Log::create_stream(LoL::LOG, [$columns=Info, $path="LoL"]);
    }

redef record dns += {
    league_of_legends: Info &optional;
    }

event foo(){
    
   local lol_flags = vector("harbinger.leagueoflegends.com", "ekg.riotgames.com", "auth.riotgames.com", "statis.leagueoflegends.com");
   local short_flag = "ekg.riotgames.com";
   local query_data = 

   if (short_flag in query_data );
    }
