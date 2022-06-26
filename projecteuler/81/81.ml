
let load_file () = 
  let f = open_in "projecteuler/81/p081_matrix.txt" in
    let rec read () =
      try (
        let l = input_line f 
        |> String.split_on_char ',' 
        |> Array.of_list
        |> Array.map int_of_string in
        l::read ()
      )
    with End_of_file -> [] in
    read () |> Array.of_list;;

let sol_81 () =
  let m = load_file () in
  let n, p = Array.length m, Array.length m.(0) in
  let dp = Array.make_matrix n p 0 in
  dp.(0).(0) <- m.(0).(0);
  for i = 1 to n - 1 do
    dp.(i).(0) <- m.(i).(0) + dp.(i - 1).(0)
  done;
  for j = 1 to p - 1 do
    dp.(0).(j) <- m.(0).(j) + dp.(0).(j - 1)
  done;
  for i = 1 to n - 1 do
    for j = 1 to p - 1 do
      dp.(i).(j) <- m.(i).(j) + min (dp.(i - 1).(j)) (dp.(i).(j - 1))
    done
  done;
  dp.(n - 1).(p - 1);;