use std::time::Instant;
use std::fs;
use fs::read_to_string;
use std::error::Error;
fn overlapping_ranges(ranges: &Vec<(u64, u64)>) -> u64 {
    let mut events: Vec<(u64, i32)> = Vec::<(u64, i32)>::new();
    let mut sweep = 0;
    let mut count :u64 = 0;
    for &(start, end) in ranges.iter() {
        events.push((start, 1));
        events.push((end + 1 , -1));
    }
    events.sort_by(|a, b| a.0.cmp(&b.0));
    let mut last = events[0].0;
    let mut last_sweep = sweep;
    for (cord, bias) in events{
        sweep += bias;
        if sweep < last_sweep{
            count+= cord - last;
        }
        if sweep < last_sweep || last_sweep == 0 {
            last = cord;
        }
        last_sweep = sweep;
    }
    count
}

fn main() -> Result<(), Box<dyn Error>> {
    let content =  read_to_string("input.txt")?;
    let lines: Vec<&str> = content.lines().collect();
    let (ranges_tmp, fresh_ids_tmp): (Vec<&str>, Vec<&str>) = lines.iter().filter(|&l| !l.is_empty()).partition(|&l| l.contains("-"));
    let ranges = ranges_tmp.into_iter().map(|line|{
        let separated = line.split("-").collect::<Vec<&str>>();
        (separated[0].parse::<u64>().unwrap(), separated[1].parse::<u64>().unwrap())
    }).collect::<Vec<(u64, u64)>>();
    let fresh_ids = fresh_ids_tmp.into_iter().map(|line|line.parse::<u64>().unwrap()).collect::<Vec<u64>>();
    let now = Instant::now();
    let count = fresh_ids.into_iter().filter(|&id| {
        ranges.iter().any(|&(start,end)| start <= id && id <= end)
    }).count();
    println!("{}", count);
    println!("{}",overlapping_ranges(&ranges));
    println!("Elapsed: {} [μs]", now.elapsed().as_micros());
    Ok(())
}
