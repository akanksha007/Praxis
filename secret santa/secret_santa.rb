require 'csv'
def get_data_from_csv(csvname)
  headers = CSV.open(csvname, 'r') { |csv| csv.first }
  person_details = CSV.read(csvname)
  person_details - [headers]
  headers.push("santa.email")
  print person_details
  person_details 
end

def select_santa(options ={})
  person_details = options.dup
  person_details.each do |option|
    x = options.sample
    while x[1] == option[1]
      x = options.sample
    end
    option.push(x[2])
    options - x
  end
  person_details
end

def put_data_to_csv(filename, data)
  CSV.open(filename, 'w') do |csv|
    data.each do |row|
      csv << row
    end
  end
end

person_array = get_data_from_csv("santas.csv")
person_array_added_santa=select_santa(person_array)
